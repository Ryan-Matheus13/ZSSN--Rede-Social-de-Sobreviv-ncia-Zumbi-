var url;

$(document).ready(() => {
  ativarItemMenu();
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

const abrirModalTroca = () => {
  $("#modal-trocar").modal(
    {
      fadeDuration: 100,
    },
    "show"
  );
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
        type: "GEt",
        success: function (data) {
          data.results.map((item, index) => {
            if (token == item.token) {
              idSobrevivente = item.id;

              // requisicoes para busca de dados
              $.ajax({
                url: "http://127.0.0.1:8000/api/itens-inventario?format=json",
                type: "GEt",
                success: function (data) {
                  data.results.map((item, index) => {
                    if (idSobrevivente == item.sobrevivente) {
                      inventario.push(item);
                    }
                  });

                  $.ajax({
                    url: "http://127.0.0.1:8000/api/itens?format=json",
                    type: "GEt",
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

                      $.ajax({
                        url: "http://127.0.0.1:8000/api/grupo-itens?format=json",
                        type: "GEt",
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
                    },
                  });
                },
              });
            }
          });
        },
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

  $("#modal-inventario").modal("show");
};

const fecharModalInventario = () => {
  console.log("gsfbsf")
  setTimeout(() => {
    $("#modal-inventario").modal("hide");
  }, 200);
};
