% include("header.tpl")
<body>
% include("menu_bar.tpl")
<div class ="container">
  <h3>こんにちは、{{name}}さん。
  <small>性別:{{sex}}, 身長:{{height}} [cm]</small></h3>
</div>

<!-- 歩数に関する表示 -->
<div class ="container">
  <div class="container-fluid">
    <div class="row">
      <div class="col-md-8 col-lg-8">
        <p>今日の歩数は…</p>
        <div class="col-md-12 col-lg-12">
          <div id="msgid1"></div>
        </div>
        <div class="col-md-12 col-lg-12">
          <div id="msgid2"></div>
        </div>
      </div>
      <div class="col-md-4 col-lg-4">
        <Center>
        {{!lev_img}}
        </Center>
      </div>
    </div>
  </div>
</div></br></br>

<div class="container"><legend>詳細</legend><!-- 詳細表示 -->
  <div class="container">
    <div class="row">
      <div class="col-lg-8"><!-- グラフの描画-->
        <div class="container">
          <div class="table-responsive">
            <script src="/js/ccchart.js" charset="utf-8"></script>
            <canvas id="today-graph"></canvas>
          </div>
        </div>
        <Center>
          <form name="form1" action="">
            <label class="checkbox-inline" for="Checkbox1">
              <input id="Checkbox1" type="checkbox" checked="checked"/>移動距離</label>
            <label class="checkbox-inline" for="Checkbox2">
              <input id="Checkbox2" type="checkbox" checked="checked"/>歩数</label>
              <input type="button" value="選択" onclick="onButtonClick(
                {{!span['date']}},
                {{graph_dataset['distance']}},
                {{graph_dataset['hosu']}}
              );" />
          </form>
        </Center>
      </div>

      <div class="col-md-4 col-lg-4 danger">
        <table class="table">
          <tr class="active">
            <td>移動距離</td>
            <td>{{int(table_dataset['sum_distance'])}} [km] </td>
            </tr>
            <td>歩数合計</td>
            <td>{{int(table_dataset['sum_hosu'])}} [歩] </td>
          </tr>
        </table>
      </div>
    </div>
  </div>
</div>

% include("footer.tpl")

<script type="text/javascript" src="/js/graph.js" charset="utf-8"></script>
<script type="text/javascript" charset="utf-8">
	onButtonClick(
		{{!span['date']}},
		{{graph_dataset['distance']}},
		{{graph_dataset['hosu']}},
	);
</script>

<script> // 文字点滅

  flg=0;
  function setMsgTenmetu(){
    if(flg < 6 & flg % 2 == 0){
      document.getElementById("msgid1").innerHTML="<h2><Center>{{int(table_dataset['sum_hosu'])}}歩です♪♪</Center></h2>";
    }
    else if (flg < 6 & flg % 2 == 1){
      document.getElementById("msgid1").innerHTML="<h2><Center></Center></h2>";
    }
    else {
      document.getElementById("msgid1").innerHTML="<h2><Center>{{int(table_dataset['sum_hosu'])}}歩です♪♪</Center></h2>";
    }
    flg += 1;
    setTimeout("setMsgTenmetu()",500);
  }
  setMsgTenmetu();
</script>

<script> // 遅延表示

  flg2=0;
  function setMsgDelay(){
    if(flg2 < 7){
      document.getElementById("msgid2").innerHTML="<Center>...診断中...</Center>";
    }
    else {
      document.getElementById("msgid2").innerHTML="{{!lev_msg}}";
    }
    flg2 += 1;
    setTimeout("setMsgDelay()",500);
  }
  setMsgDelay();
</script>

</body>
</html>

</body>
</html>
