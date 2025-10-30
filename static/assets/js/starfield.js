var layerCount = 5;
var starCount = 500;
var maxTime = 5000;

var universe = document.getElementById("universe");

for (var i = 0; i < starCount; i++) {
    var star = document.createElement("div");
    var w = document.body.clientWidth;
    var h = document.body.clientHeight;

    var xpos = Math.random() * w;
    var ypos = Math.random() * h;

    star.className = "star" + Math.floor(Math.random() * 4);
    star.style.left = xpos + "px";
    star.style.top = ypos + "px";

    universe.appendChild(star);

    star.animate(
        [
            { transform: "translateZ(0) scale(1)" },
            { transform: "translateZ(200px) scale(0)" }
        ],
        {
            duration: 2000 + Math.random() * 3000,
            iterations: Infinity
        }
    );
}