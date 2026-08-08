# Generate coverage data.
bazel coverage --combined_report=lcov --instrumentation_filter="^//python/src" //python/test/tkts

# Generate a coverage report.
genhtml -o reports/python/coverage "$(bazel info output_path)/_coverage/_coverage_report.dat"

