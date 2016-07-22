'use strict';

var buildApp = angular.module('buildrModule', [ 'ngResource' ]);

buildApp.config(function($routeProvider) {
	$routeProvider.when('/builds', {
		controller : 'BuildListCtrl',
		templateUrl : 'views/build/list.html'
	}).when('/builds/add', {
		controller : 'BuildAddCtrl',
		templateUrl : 'views/build/detail.html'
	}).when('/builds/:id', {
		controller : 'BuildEditCtrl',
			templateUrl : 'views/build/detail.html'
	}).otherwise({
		redirectTo : '/builds'
	});
});
