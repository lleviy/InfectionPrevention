//import osmeRegions from 'osme';
//const { osmeRegions } = require('osme')


// Функция ymaps.ready() будет вызвана, когда
// загрузятся все компоненты API, а также когда будет готово DOM-дерево.


ymaps.ready(init);

function init() {
  // Создание карты.
  // https://tech.yandex.ru/maps/doc/jsapi/2.1/dg/concepts/map-docpage/
  var myMap = new ymaps.Map("map", {
    // Координаты центра карты.
    // Порядок по умолчнию: «широта, долгота».
    center: [55.76, 37.64],
    // Уровень масштабирования. Допустимые значения:
    // от 0 (весь мир) до 19.
    zoom: 12,
    // Элементы управления
    // https://tech.yandex.ru/maps/doc/jsapi/2.1/dg/concepts/controls/standard-docpage/
    controls: [
      "zoomControl", // Ползунок масштаба
      "rulerControl", // Линейка
      "routeButtonControl", // Панель маршрутизации
      "trafficControl", // Пробки
      "typeSelector", // Переключатель слоев карты
      "fullscreenControl", // Полноэкранный режим

      // Поисковая строка
      new ymaps.control.SearchControl({
        options: {
          // вид - поисковая строка
          size: "large",
          // Включим возможность искать не только топонимы, но и организации.
          provider: "yandex#search"
        }
      })
    ]
  });

  var geoMap=myMap, collection=0;
  //debugger;
    // request Moscow
  window.osme.geoJSON('RU-MOW', {lang: 'ru'}, function (data) {
  var collection = window.osme.toYandex(data, ymaps);
  console.log("collection>>>>>>>", collection.properties);
  collection.add(geoMap);

  geoMap.setBounds(collection.collection.getBounds(), {duration: 300});

  var strokeColors = [
    "#F00",
    '#F0F',
    '#00F',
    '#0FF',
];
var meta = data.metaData,
    maxLevel = meta.levels[1] + 1;
    console.log(data.metaData);
    
// colorize the collection    
collection.setStyles(function (object, yobject) {
    var level = object.properties.level;
    //console.log("object>>>>>>>>>", object);
    console.log("level>>>>>>>>>", level);
    console.log("maxLevel>>>>>>>>>", maxLevel);
    console.log(strokeColors[maxLevel - level])
    return ({
        zIndex: level,
        zIndexHover: level,
        strokeWidth: Math.max(1, level == 2 ? 2 : (maxLevel - level)),
        strokeColor: strokeColors[maxLevel - level] || '#000',
        //strokeColor: strokeColors[1] || '#000',
        //fillColor: '#FFE2',
        fillColor: '#6961b0',
        fillOpacity: 0.1,
    });
  })
  })
    // Добавление метки
    // https://tech.yandex.ru/maps/doc/jsapi/2.1/ref/reference/Placemark-docpage/
    var myPlacemark = new ymaps.Placemark([55.76, 37.64], {
      // Хинт показывается при наведении мышкой на иконку метки.
      hintContent: "Содержимое всплывающей подсказки",
      // Балун откроется при клике по метке.
      balloonContent: "Содержимое балуна"
    });

  // ymaps.borders.load('RU-MOW', {
  //   lang: "en",
  //   quality: 2
  // }).then(function (geojson) {
  //   for (var i = 0; i < geojson.features.length; i++) {
  //     var geoObject = new ymaps.GeoObject(geojson.features[i]);
  //     myMap.geoObjects.add(geoObject);
  //   }
    
  // });
  // После того как метка была создана, добавляем её на карту.
  myMap.geoObjects.add(myPlacemark);
}
