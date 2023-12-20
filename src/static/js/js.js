const proyectos=document.querySelector(".proyectos");
const btn_menu=document.querySelector(".btn_menu");
const menu=document.querySelector(".menu");
btn_menu.addEventListener("click",()=>{
    menu.classList.toggle("ocultar_menu");
    btn_menu.classList.toggle("icon-menu");
    btn_menu.classList.toggle("icon-close");
});

// proyectos.addEventListener("click",(e)=>{
//     console.log(e.target.dataset["slideTo"]);
//     console.log(e.target.dataset);
//     // console.log(e.target.attributes);
//     if(e.target.dataset.hasOwnProperty("slideTo")){
//         console.log(e.target.parentNode.children);
//         console.log("encontrado");
//         let lista=Object.values(e.target.parentNode.children);
//         lista.forEach(item=>{
//             console.log(item);
//             if(item.classList.contains("active")){
//                 item.classList.remove("active");
//             }
//         })
//         e.target.classList.add("active");
//     }
// });
const nombre = document.getElementById("campo_nombre");
const email = document.getElementById("campo_email");
const expresion = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
document.getElementById("form_contact").addEventListener("submit", function (event) {
    const text_nombre=nombre.value;
    const text_email=email.value;
    if (text_nombre === "" || text_email === ""||!expresion.test(text_nombre)) {
      alert("Por favor, complete todos los campos obligatorios.");
      event.preventDefault(); // Evita que se envíe el formulario
    }
});
  






// function efectoCarrusel(){
//     if(e.target.dataset.hasOwnProperty("slideTo")){
//         console.log(e.target.parentNode.children);
//         console.log("encontrado");
//         let lista=Object.values(e.target.parentNode.children);
//         lista.forEach(item=>{
//             console.log(item);
//             if(item.classList.contains("active")){
//                 item.classList.remove("active");
//             }
//         })
//         e.target.classList.add("active");
//     }
// }