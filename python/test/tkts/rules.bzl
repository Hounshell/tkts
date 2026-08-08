load("@rules_python//python:defs.bzl", "py_test")
load("@pip//:requirements.bzl", "requirement")


def generate_py_tests(name, src_files, test_files, deps = []):
  """Dynamically generates a py_test target for every file in test_files."""

  generated_targets = []

  for test_file in test_files:
    target_name = name + '/' + test_file[:-3]
    generated_targets.append(target_name)

    py_test(
      name = target_name,
      srcs = [test_file],
      main = test_file,
      data = src_files,
      deps = deps + [
        requirement("pytest"),
      ],
    )

  native.test_suite(
    name = name,
    tests = generated_targets,
  )
