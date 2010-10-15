Map {
  map-bgcolor: transparent;
}

.boundary {
  /*line-cap: round;
  line-color: #ffffff;
  line-join: round;
  line-width: 20;*/
  polygon-fill: #ffffff;
  polygon-opacity: 0.7;

}

.road {
  line-cap: round;
  line-color: #000000;
  line-join: round;
  line-width: 5;
}

.road[zoom>=15] {
  line-width: 3;
  line-opacity: 0.7;
}

.road[zoom<15] {
  line-width: 3;
}

.road[zoom<15][USE='Arterial'] {
  line-width: 5;
}

.road[zoom>=15][USE='Arterial'] {
  line-width: 5;
  line-opacity: 1.0;
}

/* == ROAD LABELS ======================================= */
.road.label[zoom>=15][USE='Arterial'] HBLOCK {
  text-face-name: "DejaVu Sans Book";
  text-fill: #fff;
  text-halo-fill: #fb7505;
  text-halo-radius: 8;
  text-max-char-angle-delta: 20;
  text-min-distance: 100;
  text-placement: point;
  /*text-placement: line; */
  text-size: 12;
  text-spacing: 400;
}
