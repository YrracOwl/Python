    function check(){
        window.history.back();
      }
      $('#buttonZhuang').click(function(){
        var firstTime = $("#firstTime").val();
        var secondTime = $("#secondTime").val();
        var thirdTime = $("#thirdTime").val();
        var forthTime = $("#forthTime").val();
        var fifthTime = $("#fifthTime").val();
        var sixthTime = $("#sixthTime").val();

        var month = $("#monthName").val();
        var day = $("#dayname").val();

        var month_today = calendar.solar2lunar().gzMonth;
        var day_today = calendar.solar2lunar().gzDay;

        new QWebChannel(qt.webChannelTransport, function (channel) {
          window.handler = channel.objects.handler;
          window.handler.times_1(firstTime);
          window.handler.times_2(secondTime);
          window.handler.times_3(thirdTime);
          window.handler.times_4(forthTime);
          window.handler.times_5(fifthTime);
          window.handler.times_6(sixthTime);
          window.handler.times_m(month);
          window.handler.times_d(day);
          window.handler.times_m_today(month_today);
          window.handler.times_d_today(day_today);
          window.handler.dealWithIt();
        });
      });