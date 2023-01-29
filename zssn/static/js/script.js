$(document).ready(() => {
  ativarItemMenu();
});

const ativarItemMenu = () => {
  let url;
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
