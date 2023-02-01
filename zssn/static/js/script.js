var url;
var idSobreviventeSolicitado;
var csrf_token = $("#csrf_token").val();

$(document).ready(() => {
  ativarItemMenu();
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
                title: "Atenção",
                text: "Token não encontrado na base de dados!",
              }).then(() => {
                $(".jquery-modal").css("display", "none");
              });
            }
          });
        },
      }).then(() => {
        console.log(idSobreviventeSolicitado, idSobrevivente);
        if (idSobrevivente) {
          if (idSobreviventeSolicitado == idSobrevivente) {
            Swal.fire({
              icon: "warning",
              title: "Atenção",
              text: "Você não pode trocar itens com você mesmo!",
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
                      title: "Atenção",
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
      $.ajax({
        url: "http://127.0.0.1:8000/api/infectados?format=json",
        type: "GET",
        success: function (data) {
          if (data.results.length >= 1) {
            data.results.map((item, index) => {
              if (item.sobrevivente == idSobreviventeSolicitado) {
                if (item.denuncia == 3) {
                  atualizarInfectado(idSobreviventeSolicitado);
                } else {
                  denunciarSobrevivente(
                    idSobreviventeSolicitado,
                    item.denuncias
                  );
                }
              } else {
                denunciarSobrevivente(idSobreviventeSolicitado);
              }
            });
          } else {
            denunciarSobrevivente(idSobreviventeSolicitado, (modo = "insert"));
          }
        },
      });
    },
  });
};

const atualizarInfectado = (id) => {
  $("#infectadoinp").val(true);
  formData = new FormData();
  // formData.append("", "");

  $.ajax({
    url: `http://127.0.0.1:8000/api/sobreviventes/` + id + '/',
    data: formData,
    type: "PUT",
    success: function (data) {
      console.log("atualizado para infectado");
    },
  });
};

const denunciarSobrevivente = (id, quantDenuncias = 0, modo = "update") => {
  if (modo == "insert") {
    $("#denunciasinp").val(1);
    $("#sobreviventeInp").val(id);

    formData = new FormData(document.getElementById("denuncia-form"));

    $.ajax({
      url: "http://127.0.0.1:8000/api/infectados",
      data: formData,
      type: "POST",
      success: function (data) {
        console.log("inserido");
      },
    });
  } else {
    $("#denunciasinp").val(quantDenuncias + 1);
    let denuncias = $("#denunciasinp").val();

    formData = new FormData(document.getElementById("denuncia-form"));

    if (denuncias == 3) {
      $.ajax({
        url: `http://127.0.0.1:8000/api/infectados/` + id + '/',
        data: formData,
        type: "PUT",
        success: function (data) {
          console.log("atualizado");
        },
      });
      atualizarInfectado(id);
    } else {
      $.ajax({
        url: `http://127.0.0.1:8000/api/infectados/` + id + '/',
        data: formData,
        type: "PUT",
        success: function (data) {
          console.log("atualizado");
        },
      });
    }
  }
};
