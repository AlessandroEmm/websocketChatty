var app = angular.module('angularjs-starter', []).config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[').endSymbol(']}');
});

app.controller('chatWindow', function chatWindow($scope) {
  
  $scope.messages = {} 
 
  $scope.init = function() {

    $scope.ws = new WebSocket("ws://localhost:8888/chat")
    $scope.ws.onopen = function () { console.log("Connection Open") } 
    $scope.ws.onerror = function (e) { console.log("Connection has an error:" + e) }
    $scope.ws.onmessage = function (msg) { 

      var data = JSON.parse(msg.data)
      console.log(data)
      $scope.$apply(function(){
        $scope.messages[Date.now().toString()] = {"date": Date.now(), "msg": data.msg, "username": data.username}
      });

     }
  };

  $scope.sendMsg = function () {
    $scope.ws.send(JSON.stringify({"msg": $scope.msg, "username": $scope.username}))
    console.log("Sent!")
  }
 
})