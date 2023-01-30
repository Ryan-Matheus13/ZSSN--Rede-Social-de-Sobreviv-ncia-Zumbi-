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
  console.log("abriu");
};

$("#token-btn").on("click", (event) => {
  event.preventDefault();

  let token = $("#token").val()

  $.ajax({
    url: "http://127.0.0.1:8000/api/sobreviventes?format=json",
    type: "GEt",
    // data: $("#token-form").serialize(),
    success: function (data) {
      console.log(data.results);
      data.results.map((item, index) => {
        if (token == item.token) {
          console.log("achou")
        } 
      })
    },
  });
});
