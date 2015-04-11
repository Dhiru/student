angular.module('mainApp', [])
    .controller('StudentListController', ['$scope', 'mainService', function($scope, mainService)
            {
                $scope.showStudentList = false;
                $scope.showAddBehaviour = false;
                $scope.showAddStudent = false;
                $scope.user_list = [];
                $scope.behaviour_list = [];
                $scope.behaviour_user_list = [];
                $scope.output = "";
                $scope.selectStudent = "";
                $scope.selectBehaviour = "";
                $scope.user = {
                    name: "",
                    age: "",
                    class: "",
                    selectStudent: "",
                    selectBehaviour: ""
                };

                $scope.showTab = function (studentList, addBehaviour, Addstudent) {
                    $scope.showStudentList = studentList;
                    $scope.showAddBehaviour = addBehaviour;
                    $scope.showAddStudent = Addstudent;
                };

                $scope.getStudents = function(){
                    $scope.output = "";
                    mainService.getStudents().then(function (data){
                         $scope.user_list = data.users;
                    });

                };

                $scope.addBehaviour = function () {
                    var dataPost = new FormData();
                    dataPost.append('student', $scope.user.selectStudent);
                    dataPost.append('behaviour', $scope.user.selectBehaviour);

                    mainService.addBehavior(dataPost).then(function (data){
                        $scope.output = data.message;
                    });
                };

                $scope.getStudentsAndBehaviours = function(){
                    $scope.output = "";
                    mainService.getStudentsAndBehaviours().then(function (data){
                        $scope.behaviour_user_list = data.students;
                        $scope.behaviour_list = data.behaviours;
                    });
                };

                $scope.addStudent = function () {
                    var dataPost = new FormData();
                    dataPost.append('name', $scope.user.name);
                    dataPost.append('age', $scope.user.age);
                    dataPost.append('class', $scope.user.class);
                    mainService.addStudent(dataPost).then(function (data){
                        if(data.success)
                            $scope.output = data.message;
                    })
                };

            }]);
