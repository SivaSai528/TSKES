$("#file-upload").css("opacity", "0");

$("#file-browser").click(function (e) {
  e.preventDefault();
  $("#file-upload").trigger("click");
});
document.querySelector(".submitDoc").addEventListener("click", () => {
    document.querySelector("#upload-message").style.display = "block";
    document.body.style.cursor = "wait";
    document.querySelector(".wrapper").style.cursor = "wait";
    document.querySelector(".submitDoc").innerHTML = "Please wait..."
    document.querySelector(".upload-container").style.opacity = "0.3"; 
});
const fileInput = document.querySelector(
  "input[type=file]"
);
fileInput.onchange = () => {
  if (fileInput.files.length > 0) {
    const fileName = document.querySelector(".file-name");
    const uploadedFileName = fileInput.files[0].name;
    document.querySelector('.choose-file-label').style.display = "none";
    fileName.textContent = uploadedFileName;

    if (uploadedFileName.includes(".pdf")) {
      document.querySelector(".pdf").classList.add('pdficon')
      document.querySelector(".txt").classList.remove('txticon')
    }

    else if (uploadedFileName.includes(".txt")) {
      document.querySelector(".txt").classList.add('txticon')
      document.querySelector(".pdf").classList.remove('pdficon')

    }
  }
};


var app = angular.module('myApp', []);

app.controller('AppCtrl', ['$scope', '$http', '$timeout', function($scope, $http, $timeout) {
  
  // Load the data
  $http.get('http://www.corsproxy.com/loripsum.net/api/plaintext').then(function (res) {
		$scope.loremIpsum = res.data;
    $timeout(expand, 0);
  });
  
  $scope.autoExpand = function(e) {
        var element = typeof e === 'object' ? e.target : document.getElementById(e);
    		var scrollHeight = element.scrollHeight -60; // replace 60 by the sum of padding-top and padding-bottom
        element.style.height =  scrollHeight + "px";    
    };
  
  function expand() {
    $scope.autoExpand('TextArea');
  }
}]);


