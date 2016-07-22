'use strict';

buildApp.controller('BuildListCtrl', function ($scope, Build) {
	$scope.builds = Build.query();

	$scope.selectBuild = function(row) {
		$scope.selectedRow = row;
	};
	
	$scope.deleteBuild = function(build, index) {
		build.$delete();
		$scope.builds.splice(index, 1)
	}
});

buildApp.controller('BuildAddCtrl', function($scope, $location, Build) {
	
	
	$scope.saveBuild = function() {
		var current_time = new Date();
		$scope.build.build_date = current_time.getTime();
		
		Build.save($scope.build, function() {
			$location.path('/builds');
		});
	};
});

buildApp.controller('BuildEditCtrl', function($scope, $location, $routeParams,
		Build) {
	$scope.build = Build.get({
		id : $routeParams.id
	});
	
	$scope.saveBuild = function() {
		$scope.build.$update();
		$location.path('/builds')
	}
});