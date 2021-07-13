import sys
sys1 = sys.argv[1]
sys2 = sys.argv[1]
print("<div id=\"center\"><div id=\"content\"><br><br><br><div id=\"container\"></div><p style=\"color:white;text-align:center;font-family: opnsans;font-size:30px;padding: 10px 0px 10px 0px;border-style: solid;\" id=\"txt\">"+sys2+"</p></div></div><script src=\"ruffle.js\"></script><script>window.RufflePlayer=window.RufflePlayer||{};window.addEventListener(\"load\",(event)=>{const ruffle=window.RufflePlayer.newest();const player=ruffle.createPlayer();const container=document.getElementById(\"container\");container.appendChild(player);player.load(\"" + sys1 + "\");});</script><style>@font-face {font-family: opnsans;src: url(opnsans.ttf);}body{background-color: #000000;}#content {width: 37%;margin: 0 auto;}</style>")
