import sys
sys1 = sys.argv[1]
sys2 = sys.argv[1]
print("<div id=center><div id=content class=txt><br><br><br><div id=container></div><p id=txtid style=\"color:#fff;text-align:center;font-family:opnsans;font-size:30px;padding:10px 0 10px 0;border-style:solid\">" + sys1 + "</p><button class=btn id=btnid onclick='sw(\"txt\",\"29.5%\")'style=\"color:#fff;text-align:center;font-family:opnsans;font-size:30px;padding:10px 0 10px 0;border-style:20px solid #fff;background-color:#000;border-color:#fff;width:100%;margin:0 auto;border-width:3px\">Switch to Computer Mode</button></div></div><script src=ruffle.js></script><script>window.RufflePlayer = window.RufflePlayer||{};window.addEventListener(\"load\", (event) => {const ruffle = window.RufflePlayer.newest();const player = ruffle.createPlayer();const container = document.getElementById(\"container\");container.appendChild(player);player.load(\"" + sys2 + "\");});function sw(cl, v){var a=document.getElementsByClassName(cl);for (var i=0;i<a.length;i++) a[i].style.width=v;}</script><style>@font-face{font-family:opnsans;src:url(opnsans.ttf)}body{background-color:#000}#content{width:37%;margin:0 auto}</style>")
