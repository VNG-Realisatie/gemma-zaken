'use strict';
var gulp = require('gulp');
var paths = require('../paths');


/**
 * Watch task
 * Run using "gulp watch"
 * Runs "watch-js" and "watch-sass" tasks
 */
gulp.task('watch', ['sass', 'watch-sass']);


/**
 * Watch-sass task
 * Run using "gulp watch-sass"
 * Runs "sass" task instantly and when any file in paths.sassSrc changes
 */
gulp.task('watch-sass', ['sass'], function() {
    gulp.watch(paths.sassSrc, ['sass']);
});
