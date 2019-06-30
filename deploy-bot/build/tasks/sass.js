'use strict';
var cleanCSS = require('gulp-clean-css');
var gulp = require('gulp');
var sass = require('gulp-sass');
var autoprefixer = require('gulp-autoprefixer');
var purge = require('gulp-css-purge');
var paths = require('../paths');


/**
 * Sass task
 * Run using "gulp sass"
 * Searches for sass files in paths.sassSrc
 * Compiles sass to css
 * Includes bourbon neat
 * Auto prefixes css
 * Writes css to paths.cssDir
 */
gulp.task('sass', ['font-awesome'], function() {
    // Searches for sass files in paths.sassSrc
    return gulp.src(paths.sassSrc)
        // Compiles sass to css
        .pipe(sass({
            outputStyle: 'compressed',

            // Allow importing from node_modules in .scss files
            includePaths: 'node_modules/',
        })
        .on('error', sass.logError))

        // Auto prefixes css
        .pipe(autoprefixer({
            browsers: ['last 2 versions'],
            cascade: false
        }))

        // Remove duplicated code
        .pipe(purge())
        .pipe(cleanCSS({compatibility: 'ie8', level: 2}))

        // Writes css to paths.cssDir
        .pipe(gulp.dest(paths.cssDir));
});
