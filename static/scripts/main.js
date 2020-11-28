// Readying jquery

$(document).ready(function () {
    // All code goes here 

    // Update navbar in other files based on index.html navbar
    console.log($("div.navbar").load("static/assets/navbar.html"));
})