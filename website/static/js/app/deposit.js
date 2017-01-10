

    var depositApp = angular.module("deposit", []);
    depositApp.controller("depositCtrl", function($scope, $http) {
        var reload = function() {
            $http.get("/api/deposit/list").then(function(response) {
                if(response.data.resultCode == 1) {
                    $scope.depositList = response.data;
                }
                else
                {
                    alert(response.data.resultMsg);
                }
            });
        };

        reload();

        $scope.reloadClick = function() {
            reload();
        }
    });