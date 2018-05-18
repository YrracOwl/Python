      var tableA = document.getElementById("a-table").getElementsByTagName("tr");
      var guaName = document.getElementById("guaName");
      var riyue = document.getElementById("riyue");
      var presentTime = document.getElementById("presentTime");

      var h2 = document.getElementById("infoBottom");
      var flag = 'True';
      $(document).ready(function(){
        new QWebChannel(qt.webChannelTransport, function (channel) {
          window.handler = channel.objects.handler;
          //将python的返回值传回并处理！
          handler.grapData(function(message){
            flag = message;
            if (flag === 'False')
              h2.innerHTML = "请在六爻预测页面输入正确的信息！";
          });
          //向表格中填写世应
          handler.shiying(function(message){
            for (let i=1;i<7;i++){
              tableA[i].getElementsByTagName("td")[1].innerText = message[i-1];
            }
          });
          //向表格中填写卦象
          handler.orignShape(function(message){
            for (let i=1;i<7;i++){
              tableA[i].getElementsByTagName("td")[2].innerText = message[i-1];
            }
          });
          //向表格中填写六亲
          handler.liuqin(function(message){
            for (let i=1;i<7;i++){
              tableA[i].getElementsByTagName("td")[3].innerText = message[i-1];
            }
          });
          //向表格中填写干支
          handler.activeGanZhi(function(message){
            for (let i=1;i<7;i++){
              tableA[i].getElementsByTagName("td")[4].innerText = message[i-1];
            }
          });
          //向表格中填写变爻
          handler.guaBian(function(message){
            for (let i=1;i<7;i++){
              tableA[i].getElementsByTagName("td")[5].innerText = message[i-1];
            }
          });
          //向表格中填写六神
          handler.liushenPosition(function(message){
            for (let i=1;i<7;i++){
              tableA[i].getElementsByTagName("td")[6].innerText = message[i-1];
            }
          });
          //向表格中填写卦宫
          handler.guaGong(function(message){
            for (let i=1;i<7;i++){
              tableA[i].getElementsByTagName("td")[7].innerText = message[i-1];
            }
          });
          //向表格中填写伏神
          handler.liuqinGong(function(message){
            for (let i=1;i<7;i++){
              tableA[i].getElementsByTagName("td")[8].innerText = message[i-1];
            }
          });
          //向表格中填写卦宫干支
          handler.ganzhiGong(function(message){
            for (let i=1;i<7;i++){
              tableA[i].getElementsByTagName("td")[9].innerText = message[i-1];
            }
          });

          //写入卦名的变化
          handler.guaName(function(message){
            guaName.innerText = message;
          });
          //写入月份日辰的信息
          handler.riyue(function(message){
            riyue.innerText = message;
          });
          //写入当前月份与日辰
          handler.month_day(function(message){
            presentTime.innerText = message;
          });
        });
      });