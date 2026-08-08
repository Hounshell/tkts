import glob
import os
import sys
import unittest
import mypy.api

class TypeCheckTest(unittest.TestCase):
  def test_type_annotations(self):
    # Collect all python files in python/src
    src_files = glob.glob("python/src/**/*.py", recursive=True)
    
    # Ensure files were actually found in the sandbox
    self.assertTrue(len(src_files) > 0, "No Python source files found to type check.")

    # Pass explicit file list and isolation flags to mypy
    stdout, stderr, exit_status = mypy.api.run([
      "--explicit-package-bases",
      "--ignore-missing-imports",
      "--exclude", r"\.runfiles",
      "--exclude", r"_main",
    ] + src_files)
    
    self.assertEqual(
      exit_status, 
      0, 
      f"Mypy errors found:\n{stdout}\n{stderr}"
    )

if __name__ == "__main__":
  unittest.main()

