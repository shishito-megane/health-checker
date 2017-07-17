% include("header.tpl")
<body>
% include("menu_bar.tpl")
<!-- ようこそ！ -->
<div class="container">
  <h3>Welcome！<small>Keep yourself healty！</small></h3>
  <h5>下記の項目を入力し、送信ボタンを押してください</h5>
</div>
<br>

<!-- 項目表示 -->
<div class="container">
  <legend>項目</legend>
</div>

<div class="col-lg-offset-2 col-md-offset-2 col-lg-10 col-md-10">
  <form class="form-horizontal" action="/health/today">
    <fieldset>
      <!--<legend>Legend</legend>-->
      <div class="form-group"><!-- 性別選択(リスト) -->
        <label class="col-lg-2 col-md-2 control-label">
          性別
        </label>
        <div class="col-lg-3 col-md-3">
          <div class="radio">
            <label>
              <input type="radio" name="sex" id="optionsRadios1" value="man">
              男性
            </label>
          </div>
          <div class="radio">
            <label>
              <input type="radio" name="sex" id="optionsRadios2" value="woman">
              女性
            </label>
          </div>
        </div>
        <div class="col-lg-9 col-md-9">
          <!-- null -->
        </div>
      </div>

      <div class="form-group"><!-- 身長入力(フォーム) -->
        <label for="hight" class="col-lg-2 col-md-2 control-label">
          身長
        </label>
        <div class="col-lg-3 col-md-3">
          <input type="text" class="form-control" placeholder="154 [cm]" id="height" name="height">
        </div>
      </div>

      <div class="form-group"><!-- 送信ボタン -->
        <div class="col-lg-3 col-md-3 col-lg-offset-2 col-md-offset-3">
          <button class="btn btn-primary" href="{{link}}">送信</button>
        </div>
      </div>
    </fieldset>
  </form>
  </div>

</body>
</html>
