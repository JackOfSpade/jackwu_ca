

$(document).ready(function() {
  function getCookie(name) {
      let cookieValue = null;
      if (document.cookie && document.cookie !== '') {
          const cookies = document.cookie.split(';');
          for (let i = 0; i < cookies.length; i++) {
              const cookie = cookies[i].trim();
              // Does this cookie string begin with the name we want?
              if (cookie.substring(0, name.length + 1) === (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
              }
          }
      }
      return cookieValue;
  }

  const csrftoken = getCookie("csrftoken");

  function csrfSafeMethod(method) {
      // these HTTP methods do not require CSRF protection
      return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }

  $.ajaxSetup({
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      }
  });

  $("html").one( "click", function() {
    const player = $("#player")
    player.get(0).play();
    player[0].volume = 0;
    player.animate({volume: 1}, 10000);
  });

  (function () {
    var WIDTH, HEIGHT, canvas, con, g;
    var pxs = [];
    var rint = 50;

    $.fn.sprites = function () {
      this.append($('<canvas id="sprites"></canvas>'));
      setup(this);
    }

    function setup(container) {
      var windowSize = function () {
        WIDTH = container.innerWidth();
        HEIGHT = container.innerHeight();
        canvas = container.find('#sprites');
        canvas.attr('width', WIDTH).attr('height', HEIGHT);
      };

      windowSize();

      $(window).resize(function () {
        windowSize();
      });

      con = canvas[0].getContext('2d');

      for (var i = 0; i < 100; i++) {
        pxs[i] = new Circle();
        pxs[i].reset();
      }

      requestAnimationFrame(draw);
    }

    function draw() {
      con.clearRect(0, 0, WIDTH, HEIGHT);
      con.globalCompositeOperation = "lighter";

      for (var i = 0; i < pxs.length; i++) {
        pxs[i].fade();
        pxs[i].move();
        pxs[i].draw();
      }

      requestAnimationFrame(draw);
    }

    function Circle() {
      this.s = {
        ttl: 15000,
        xmax: 5,
        ymax: 2,
        rmax: 7,
        rt: 1,
        xdef: 960,
        ydef: 540,
        xdrift: 4,
        ydrift: 4,
        random: true,
        blink: true
      };

      this.reset = function () {
        this.x = (this.s.random ? WIDTH * Math.random() : this.s.xdef);
        this.y = (this.s.random ? HEIGHT * Math.random() : this.s.ydef);
        this.r = ((this.s.rmax - 1) * Math.random()) + 1;

        this.dx = (Math.random() * this.s.xmax) * (Math.random() < 0.5 ? -1 : 1);
        this.dy = (Math.random() * this.s.ymax) * (Math.random() < 0.5 ? -1 : 1);

        this.hl = (this.s.ttl / rint) * (this.r / this.s.rmax);
        this.rt = Math.random() * this.hl;

        this.stop = Math.random() * 0.2 + 0.4;

        this.s.rt = Math.random() + 1;
        this.s.xdrift *= Math.random() * (Math.random() < 0.5 ? -1 : 1);
        this.s.ydrift *= Math.random() * (Math.random() < 0.5 ? -1 : 1);
      };

      this.fade = function () {
        this.rt += this.s.rt;
      };

      this.draw = function () {
        var newo, cr;

        if (this.s.blink && (this.rt <= 0 || this.rt >= this.hl)) {
          this.s.rt = this.s.rt * -1;
        } else if (this.rt >= this.hl) {
          this.reset();
        }

        newo = 1 - (this.rt / this.hl);

        con.beginPath();
        con.arc(this.x, this.y, this.r, 0, Math.PI * 2, true);
        con.closePath();

        cr = this.r * newo;

        g = con.createRadialGradient(this.x, this.y, 0, this.x, this.y, (cr <= 0 ? 1 : cr));
        g.addColorStop(0.0, 'rgba(193,254,254,' + newo + ')');
        g.addColorStop(this.stop, 'rgba(193,254,254,' + (newo * 0.2) + ')');
        g.addColorStop(1.0, 'rgba(193,254,254,0)');

        con.fillStyle = g;
        con.fill();
      };

      this.move = function () {
        this.x += (this.rt / this.hl) * this.dx;
        this.y += (this.rt / this.hl) * this.dy;
        if (this.x > WIDTH || this.x < 0) this.dx *= -1;
        if (this.y > HEIGHT || this.y < 0) this.dy *= -1;
      };

      this.getX = function () {
        return this.x;
      };

      this.getY = function () {
        return this.y;
      };
    };
  })();

  $(".spriteWrap").sprites();

  controls = $(".controls")

  controls.hover(function(){
    controls.css({
      "transform": "translate3d(0px, 0px, 0px)",
      "opacity": "1"
    });

    $("#results_table").css({
      "margin-left": "21%"
    });
  });

  controls.mouseleave(function(){
    controls.css({
      "transform": "translate3d(-250px, 0px, 0px)",
      "opacity": "0"
    });

    $("#results_table").css({
      "margin-left": "1%"
    });
  });

  function convert_to_html(list_or_string) {
    var element;
    var html = "";
    if (Array.isArray(list_or_string)){
      for (element in list_or_string) {
        html += "<td class='results_td'>" + element + "</td>";
      }
    }
    else{
      html = "<td class='results_td'>" + list_or_string + "</td>";
    }

    return html;
  }

  $("#weather_form").on("submit", function(event){
  // $("#go").click(function(){
    //Prevent default django post behaviour for a form submission.
    event.preventDefault();

    $.ajax({
      url: "/weather/",
      type: "POST",
      data: {type_of_person: $("#id_type_of_person").val(),
        exercise: $("#id_exercise").val(),
        unit: $("#id_unit").val(),
        zip_postal: $("#id_zip_postal").val()},
      dataType: "json",
      success: function (data){
        results_matrix = data["results_matrix"];

        $("#results_table tr").remove();

        var time_html = convert_to_html(results_matrix[0][1]);
        var temperature_html = convert_to_html(results_matrix[1][1]);
        var uv_index_html = convert_to_html(results_matrix[2][1]);

        $("#results_table").append(
            "<tr>" +
              "<th>" + results_matrix[0][0] + "</th>" +
              time_html +
            "</tr>" +
            "<tr>" +
              "<th>" + results_matrix[1][0] + "</th>" +
              temperature_html +
            "</tr>" +
            "<tr>" +
              "<th>" + results_matrix[2][0] + "</th>" +
              uv_index_html +
            "</tr>");

        if (results_matrix[3][0])
        {
           $("#results_table").append(
            "<tr>" +
              "<th>" + results_matrix[3][0] + "</th>" +
            "</tr>");
        }
      },
      error: function(xhr,errmsg,err) {
        $("html").innerHTML = "";
        $("html").prepend("<body><div id='dialog'><p>" + xhr.responseText + "</p></div></body>");
        $( "#dialog" ).dialog({
          maxHeight: window.innerHeight - 15,
          overflow:"scroll"
        });
      }
    });
  });
});

