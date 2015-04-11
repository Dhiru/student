angular.module('studentApp', [])
    .controller('StudentListController', function($scope) {
	$scope.studentList = [
	    {text:'learn angular', done:true},
	    {text:'build an angular app', done:false}
	];
	$scope.abd = "sdfd";
    });

