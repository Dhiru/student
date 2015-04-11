(function () {
    'use strict';

    var serviceId = 'mainService';

    angular.module('mainApp').factory(serviceId, ['$http', '$q', mainService]);

    function mainService($http, $q) {
        var service = {
            getStudents: sendGetRequest('/students/'),
            getStudentsAndBehaviours: sendGetRequest('/getstudentsandbehaviours/'),
            addBehavior: sendPostRequest('/givepoints/'),
            addStudent: sendPostRequest('/addstudent/'),
            getHeaders: getHeaders
        };
        return service;

        function sendGetRequest(url) {
            return function (requestData) {
                var deferred = $q.defer();
                $http({
                          method: 'GET',
                          url: url,
                          params: requestData
                      }).success(function (data, status, headers, cfg) {
                    deferred.resolve(data);
                }).error(function (err, status) {
                    deferred.reject(status);
                });
                return deferred.promise;
            };
        }

        function sendPostRequest(url) {
            return function(requestData) {
                requestData.append('csrfmiddlewaretoken', csrf);
                var deferred = $q.defer();
                $.ajax({
                    url: url,
                    type: "POST",
                    data: requestData,
                    dataType: 'json',
                    processData: false,
                    contentType: false,
                    success: function (data) {
                        deferred.resolve(data);
                    },
                    error: function (error, status) {
                        deferred.reject(status);
                    }
                });
                return deferred.promise;
            };
            return deferred.promise;
        }

        function getHeaders() {
            return { "contentType": "application/json"};
        }


    }
})();
function getCookie(c_name) {
    var i, x, y, ARRcookies = document.cookie.split(";");
    for (i = 0; i < ARRcookies.length; i++) {
        x = ARRcookies[i].substr(0, ARRcookies[i].indexOf("="));
        y = ARRcookies[i].substr(ARRcookies[i].indexOf("=") + 1);
        x = x.replace(/^\s+|\s+$/g, "");
        if (x == c_name) {
            return unescape(y);
        }
    }
}