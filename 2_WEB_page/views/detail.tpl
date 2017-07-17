% include("header-map.tpl")
<body>
% include("menu_bar.tpl")

    <!--地図の表示-->
    <div id="map"></div>

% include("footer.tpl")

    <script> // Google map用
      // This example creates a 2-pixel-wide red polyline showing the path of William
      // Kingsford Smith's first trans-Pacific flight between Oakland, CA, and
      // Brisbane, Australia.

      function initMap() {
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 17,
          center: {lat: {{map_dataset['latitude'][0]}}, lng: {{map_dataset['longitude'][0]}}},               // 最初に表示した時の中央を決める
          mapTypeId: google.maps.MapTypeId.TERRAIN
        });

        var flightPlanCoordinates = [                                           // 緯度と経度を指定
          % for i in range(0,len(map_dataset['latitude'])):
            {lat: {{map_dataset['latitude'][i]}}, lng: {{map_dataset['longitude'][i]}} },
          % end
        ];
        var flightPath = new google.maps.Polyline({
          path: flightPlanCoordinates,
          geodesic: true,
          strokeColor: '#FF0000',
          strokeOpacity: 1.0,
          strokeWeight: 2
        });

        flightPath.setMap(map);
      }

    </script>
    <script async defer
        src="https://maps.googleapis.com/maps/api/js?key=AIzaSyCq-S4_EqBvck-5z_7N4taMkhEdctmoy70&callback=initMap"></script>
  </body>
</html>
