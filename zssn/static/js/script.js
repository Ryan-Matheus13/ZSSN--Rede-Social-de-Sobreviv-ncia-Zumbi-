var url;
var idSobreviventeSolicitado;
var csrf_token = $("#csrf_token").val();
var sobrevivente = {};
var itensSobrevivente = [];

$(document).ready(() => {
  ativarItemMenu();
  preencherSelectItens();
});

$("form").on("keyup keypress", function (e) {
  var keyCode = e.keyCode || e.which;
  if (keyCode === 13) {
    e.preventDefault();
    return false;
  }
});

const ativarItemMenu = () => {
  url = $("#current-url").val().substring(1);

  $(".page-item").removeClass("active");
  switch (url) {
    case "":
      $("#home").addClass("active");
      break;
    case "sobreviventes":
      $("#sobreviventes").addClass("active");
      break;
    case "mercado":
      $("#mercado").addClass("active");
      break;
    case "relatorios":
      $("#mercado").addClass("active");
      break;
    default:
      break;
  }
};

$(".btn-cancelar").on("click", () => {
  $(".modal").modal("hide");
});

const abrirModalTroca = (id) => {
  $("#modal-trocar").modal(
    {
      fadeDuration: 100,
    },
    "show"
  );

  idSobreviventeSolicitado = id;
};

const abrirModalDenuncia = (id) => {
  $("#modal-denuncia").modal(
    {
      fadeDuration: 100,
    },
    "show"
  );

  idSobreviventeSolicitado = id;
};

$("#token-btn").on("click", () => {
  buscarDadosInventario();
});

const buscarDadosInventario = () => {
  let token = $("#token").val();
  let inventario = [];
  let idSobrevivente;
  let itens = [];

  Swal.fire({
    title: "Aguarde",
    allowOutsideClick: false,
    allowEscapeKey: false,
    showConfirmButton: false,
    willOpen: () => {
      $("#modal-trocar").modal("hide");
      Swal.showLoading();
    },
    didOpen: () => {
      $.ajax({
        url: "http://127.0.0.1:8000/api/sobreviventes?format=json",
        type: "GET",
        success: function (data) {
          data.results.map((item, index) => {
            if (token == item.token) {
              idSobrevivente = item.id;
            } else if (
              token != item.token &&
              index == data.results.length - 1 &&
              !idSobrevivente
            ) {
              Swal.fire({
                icon: "warning",
                title: "Aten????o",
                text: "Token n??o encontrado na base de dados!",
              }).then(() => {
                $(".jquery-modal").css("display", "none");
              });
            }
          });
        },
      }).then(() => {
        // console.log(idSobreviventeSolicitado, idSobrevivente);
        if (idSobrevivente) {
          if (idSobreviventeSolicitado == idSobrevivente) {
            Swal.fire({
              icon: "warning",
              title: "Aten????o",
              text: "Voc?? n??o pode trocar itens com voc?? mesmo!",
            }).then(() => {
              $(".jquery-modal").css("display", "none");
            });
          } else {
            $.ajax({
              url: "http://127.0.0.1:8000/api/itens-inventario?format=json",
              type: "GET",
              success: function (data) {
                data.results.map((item, index) => {
                  if (idSobrevivente == item.sobrevivente) {
                    inventario.push(item);
                  } else if (
                    idSobrevivente != item.sobrevivente &&
                    index == data.results.length - 1
                  ) {
                    Swal.fire({
                      icon: "warning",
                      title: "Aten????o",
                      text: "Sobrevivente sem itens disponiveis!",
                    }).then(() => {
                      $(".jquery-modal").css("display", "none");
                    });
                  }
                });
              },
            }).then(() => {
              $.ajax({
                url: "http://127.0.0.1:8000/api/itens?format=json",
                type: "GET",
                success: function (data) {
                  data.results.map((item, index) => {
                    inventario.map((itemInven, index) => {
                      if (itemInven.item == item.id) {
                        itemInven.itemId = itemInven.item;
                        itemInven.item = item.nome;
                      }
                    });

                    itens.push(item);
                  });
                },
              }).then(() => {
                $.ajax({
                  url: "http://127.0.0.1:8000/api/grupo-itens?format=json",
                  type: "GET",
                  success: function (data) {
                    data.results.map((grupo, index) => {
                      itens.map((item, index) => {
                        if (item.grupo == grupo.id) {
                          inventario.map((itemInven, index) => {
                            if (itemInven.itemId == item.id) {
                              itemInven.valor = grupo.valor;
                            }
                          });
                        }
                      });
                    });

                    addLinhaTabelaInventario(inventario);
                    Swal.close();
                  },
                });
              });
            });
          }
        }
      });
    },
  });
};

const addLinhaTabelaInventario = (inventario) => {
  $("#inventario-body").remove();

  let inventarioBody = document.createElement("div");
  inventarioBody.setAttribute("id", "inventario-body");
  $("#inventario-table").append(inventarioBody);

  inventario.map((item, index) => {
    let elemento = `
                  <div class="custom-table-row">
                    <span class="custom-table-data" style="width: 50%">
                      ${item.item}
                    </span>
                    <span class="custom-table-data" style="width: 15%">
                      ${item.quantidade} Un.
                    </span>
                    <span class="custom-table-data" style="width: 15%">
                      ${item.valor} Pt.
                    </span>
                    <span class="custom-table-data" style="width: 15%">
                      ${item.valor * item.quantidade} Pt.
                    </span>
                    <span class="custom-table-data-buttons" style="width: 5%">
                      <a class="custom-table-button" id="adicionar-item-venda" title="Vender" onclick="">
                        <span class="material-symbols-outlined">add</span>
                      </a>
                    </span>
                  </div>
                  `;

    $("#inventario-body").prepend(elemento);
  });

  $("#modal-inventario").modal(
    {
      fadeDuration: 100,
    },
    "show"
  );
};

const buscarDenunciasSobrevivente = () => {
  let infectado = false;

  Swal.fire({
    title: "Aguarde",
    allowOutsideClick: false,
    allowEscapeKey: false,
    showConfirmButton: false,
    willOpen: () => {
      $("#modal-denuncia").modal("hide");
      Swal.showLoading();
    },
    didOpen: () => {
      // console.log("entrou 1");
      $.ajax({
        url: "http://127.0.0.1:8000/api/infectados?format=json",
        type: "GET",
        success: function (data) {
          if (data.results.length >= 1) {
            data.results.map((item, index) => {
              if (item.sobrevivente == idSobreviventeSolicitado) {
                infectado = item;
              }
            });
          } else {
            denunciarSobrevivente(idSobreviventeSolicitado, 1, "insert");
          }
        },
      }).then(() => {
        if (infectado == false) {
          denunciarSobrevivente(idSobreviventeSolicitado, 0, 1, "insert");
        } else {
          if (infectado.denuncias >= 3) {
            atualizarInfectado(idSobreviventeSolicitado);
          } else {
            denunciarSobrevivente(
              idSobreviventeSolicitado,
              infectado.id,
              infectado.denuncias
            );
          }
        }
      });
    },
  });
};

const atualizarInfectado = (id) => {
  let sobrevivente;
  // console.log("passou aqui");
  $.ajax({
    url: `http://127.0.0.1:8000/api/sobreviventes/` + id + "/",
    credentials: "same-origin",
    type: "GET",
    dataType: "json",
    headers: {
      "X-Requested-With": "XMLHttpRequest",
      "X-CSRFToken": csrf_token,
    },
    success: function (data) {
      sobrevivente = data;
      sobrevivente.infectado = true;
    },
  }).then(() => {
    $.ajax({
      url: `http://127.0.0.1:8000/api/sobreviventes/` + id + "/",
      credentials: "same-origin",
      type: "PUT",
      dataType: "json",
      data: sobrevivente,
      headers: {
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": csrf_token,
      },
      success: function (data) {},
    }).then(() => {
      setTimeout(() => {
        location.reload();
      }, 1000);
    });
  });
};

const denunciarSobrevivente = (
  id,
  idInfectado,
  quantDenuncias = 0,
  modo = "update"
) => {
  // console.log(modo);
  if (modo == "insert") {
    // console.log("ENTROU POST");
    $.ajax({
      url: "http://127.0.0.1:8000/api/infectados",
      credentials: "same-origin",
      type: "POST",
      dataType: "json",
      data: { denuncias: 1, sobrevivente: id },
      headers: {
        "X-Requested-With": "XMLHttpRequest",
        "X-CSRFToken": csrf_token,
      },
      success: function (data) {},
    }).then(() => {
      setTimeout(() => {
        location.reload();
      }, 1000);
    });
  } else {
    total = quantDenuncias + 1;
    // console.log(total)
    if (total == 3) {
      // console.log("entrou aqui");
      $.ajax({
        url: `http://127.0.0.1:8000/api/infectados/` + idInfectado + "/",
        credentials: "same-origin",
        type: "PUT",
        dataType: "json",
        data: { denuncias: quantDenuncias + 1 },
        headers: {
          "X-Requested-With": "XMLHttpRequest",
          "X-CSRFToken": csrf_token,
        },
        success: function (data) {
          atualizarInfectado(id);
        },
      });
    } else {
      // console.log("entrou aqui 2");
      $.ajax({
        url: `http://127.0.0.1:8000/api/infectados/` + idInfectado + "/",
        credentials: "same-origin",
        type: "PUT",
        dataType: "json",
        data: { denuncias: quantDenuncias + 1 },
        headers: {
          "X-Requested-With": "XMLHttpRequest",
          "X-CSRFToken": csrf_token,
        },
        success: function (data) {},
      }).then(() => {
        setTimeout(() => {
          location.reload();
        }, 1000);
      });
    }
  }
};

function randomizeValue() {
  var value = (1 + 10e-16) * Math.random();

  if (value > 1.0) {
    return 1.0;
  }

  return value;
}

function randomizeFloat(min, max) {
  if (max == null) {
    max = min == null ? Number.MAX_VALUE : min;
    min = 0.0;
  }
  value = min + (max - min) * randomizeValue();
  return value.toFixed(4);
}

const atualizarLoc = (id) => {
  Swal.fire({
    title: "Atualizando localiza????o",
    allowOutsideClick: false,
    allowEscapeKey: false,
    showConfirmButton: false,
    willOpen: () => {
      Swal.showLoading();
    },
    didOpen: () => {
      $.ajax({
        url: `http://127.0.0.1:8000/api/sobreviventes/` + id + "/",
        credentials: "same-origin",
        type: "GET",
        dataType: "json",
        headers: {
          "X-Requested-With": "XMLHttpRequest",
          "X-CSRFToken": csrf_token,
        },
        success: function (data) {
          sobrevivente = data;
          sobrevivente.lat = randomizeFloat(-90, 90);
          sobrevivente.long = randomizeFloat(-180, 180);
        },
      }).then(() => {
        $.ajax({
          url: `http://127.0.0.1:8000/api/sobreviventes/` + id + "/",
          credentials: "same-origin",
          type: "PUT",
          dataType: "json",
          data: sobrevivente,
          headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": csrf_token,
          },
          success: function (data) {},
        }).then(() => {
          setTimeout(() => {
            location.reload();
          }, 1000);
        });
      });
    },
  });
};

const preencherSelectItens = () => {
  let itens;
  $.ajax({
    url: "http://127.0.0.1:8000/api/itens?format=json",
    type: "GET",
    success: function (data) {
      itens = data.results;
    },
  }).then(() => {
    itens.map((item, index) => {
      let elemento = `
                  <option value="${item.id}">
                    ${item.nome}
                  </option>
                  `;
      $("#select-item").append(elemento);
    });
  });
};

const abrirModalCadastroSobrevivente = () => {
  $("#modal-cadastro").modal({ fadeDuration: 100 }, "show");
};

const adicionarItem = () => {
  let itemId = $("#select-item").val();
  let quantItem = $("#quantidade-sobrevivente").val();
  let item;

  if (itemId == "" || quantItem == "") {
    Swal.fire({
      icon: "warning",
      title: "Aten????o",
      text: "Campos de itens invalidos ou vazios!",
    });
  } else {
    $.ajax({
      url: "http://127.0.0.1:8000/api/itens/" + itemId + "/",
      type: "GET",
      success: function (data) {
        item = data;
      },
    }).then(() => {
      console.log(item);
      let elemento = `
                    <div class="itens-adicionados-row">
                      <span class="item-nome">${item.nome}</span>
                      <span class="item-quantidade">${quantItem}x</span>
                    </div>
                    `;

      $("#itens-adicionados").prepend(elemento);
      console.log("aaaaaaa");
      $("#itens-adicionados").css("display", "flex");
      itensSobrevivente.push({
        item: item.id,
        quantidade: quantItem,
        sobrevivente: -1,
      });
    });
  }
};

const cadastrarSobrevivente = () => {
  let nome = $("#nome-sobrevivente").val();
  let idade = $("#idade-sobrevivente").val();
  let sexo = $("#sexo-sobrevivente").val();
  let token = $("#token-sobrevivente").val();

  let idSobrevivente;

  if (nome == "" || idade == "" || sexo == "" || token == "") {
    Swal.fire({
      icon: "warning",
      title: "Aten????o",
      text: "Campos de sobrevivente invalidos ou vazios!",
    });
  } else {
    Swal.fire({
      title: "Cadastrando sobrevivente",
      allowOutsideClick: false,
      allowEscapeKey: false,
      showConfirmButton: false,
      willOpen: () => {
        $("#modal-cadastro").modal("hide");
        Swal.showLoading();
      },
      didOpen: () => {
        $.ajax({
          url: "http://127.0.0.1:8000/api/sobreviventes",
          credentials: "same-origin",
          type: "POST",
          dataType: "json",
          data: {
            nome,
            idade,
            sexo,
            token,
            infectado: false,
            lat: randomizeFloat(-90, 90),
            long: randomizeFloat(-180, 180),
          },
          headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": csrf_token,
          },
          success: function (data) {},
        }).then(() => {
          $.ajax({
            url: "http://127.0.0.1:8000/api/sobreviventes?format=json",
            type: "GET",
            success: function (data) {
              data.results.map((item, index) => {
                if (token == item.token) {
                  idSobrevivente = item.id;
                }
              });
            },
          }).then(() => {
            itensSobrevivente.map((item, index) => {
              item.sobrevivente = idSobrevivente;
              $.ajax({
                url: "http://127.0.0.1:8000/api/itens-inventario",
                credentials: "same-origin",
                type: "POST",
                dataType: "json",
                data: item,
                headers: {
                  "X-Requested-With": "XMLHttpRequest",
                  "X-CSRFToken": csrf_token,
                },
                success: function (data) {},
              });
            });
          });
        });
      },
    });

    location.reload();
  }
};
