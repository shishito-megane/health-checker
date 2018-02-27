function onButtonClick(
  date,distance,hosu
) {

  // 見出しの設定 (リストの1つ目が見出し)
  date_dis = ['時刻']
  // 日付のみ別指定
  date_dis = date_dis.concat(date)

	// 累積活動距離
  var chartdata98 = {
    "config": {
      "title":          "きょうの活動量",
      //"subTitle":       "",
      "width":          750,
      "height":         500,
      "xScaleRotate":   -90,     // 角度 (0で水平、-45で右肩上がり80、-90で直角)
      "xScaleYOffset":  50,      // チャート領域との間隔
      "paddingBottom":  100,     // チャートの下パディング。水平軸目盛りの縦幅
      "roundDigit":     1,       // 軸目盛値の端数処理
      "type":           "line",
      "minY":           0,
      "unit":           "km",
      "useMarker":      "ring",
      "borderWidth":    5,
      "markerWidth":    12,
      "hanreiMarkerStyle": "arc",
      "colorSet":       ["#00A8A2","#666","green"],
      "shadows":        {"hanrei":["#aaa",3,3,3],"line":["#555",3,3,3]}
    },
    "data": [
              date_dis
            ]
  };

  // 1時間帯ごとの移動距離
  var chartdata4= {
    "config": {
      "title":          "きょうの活動量",
      //"subTitle":       "",
      "width":          750,
      "height":         500,
      "xScaleRotate":   -90,     // 角度 (0で水平、-45で右肩上がり80、-90で直角)
      "xScaleYOffset":  50,      // チャート領域との間隔
      "paddingBottom":  100,     // チャートの下パディング。水平軸目盛りの縦幅
      "roundDigit":     0,       // 軸目盛値の端数処理
      //"barWidth":       20,
      "type":           "stacked",
      "unit":           "歩",
      "useVal":         "no",
      "useShadow":      "no",
      "colorSet": ["rgba(0,150,250,0.6)","rgba(50,50,70,0.8)","#9acd32"],
    },

    "data": [
              date_dis
            ]
  };

  // チェックボックスの定義
  check_distance = document.form1.Checkbox1.checked
  check_hosu = document.form1.Checkbox2.checked

  // 凡例の定義
  data_distance = ['移動距離']
  data_hosu     = ['歩数']

  // 凡例の後ろにデータを結合(リストの2つ目以降がデータ)
  data_distance = data_distance.concat(distance)
  data_hosu     = data_hosu.concat(hosu)
  //グラフ要素が何も選択されなかった時の表示用空データ
  data_null     =  ['',	0	]

  // チェックボタンが押されて選択された時の挙動を定義
  if (check_distance == true) {
    chartdata98.data.push( data_distance )
  }
  else if (check_distance != true) {
    chartdata98.data.push( date_dis )
  }
  if (check_hosu == true) {
    chartdata4.data.push( data_hosu )
  }
  else if (check_hosu != true) {
    chartdata4.data.push( data_null)
  }
  if (check_distance != true && check_hosu != true){
    chartdata98.data.push( data_null )
    chartdata4.data.push( data_null )
    window.alert('なにか選択してください。');
  }

		ccchart.base("white");
		ccchart
        .init("today-graph", chartdata4)
        .after(chartdata98);
}
