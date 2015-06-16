#!/usr/bin/env python
# Usage:
#  ./test-all.py <dir for tests>

import glob
import sys
import subprocess

in_dir = "/Users/berkin/work/tmp/riscv/riscv-tests/isa/"
if len( sys.argv ) > 1:
  in_dir = sys.argv[1]

print "looking for tests in", in_dir

dumps = glob.glob( in_dir + "/*.dump" )

num_tests  = 0
num_passed = 0
num_failed = 0
num_error  = 0

for dump in dumps:
  bin_name = dump[:-5]
  try:
    out = subprocess.check_output( ["python", "riscv-sim.py", bin_name],
                                   stderr=subprocess.STDOUT )
  except subprocess.CalledProcessError as e:
    out = e.output

  num_tests += 1

  if "Pass!" in out:
    out_str = "Passed"
    num_passed += 1
  elif "Fail!" in out:
    out_str = "Failed"
    num_failed += 1
  else:
    out_str = "Error"
    num_error += 1
  test_name = bin_name[ bin_name.rfind('/')+1 : ]
  print "Test {} \t {}".format( test_name, out_str )

print "Number of tests: {} passed: {} failed: {} error: {}" \
    .format( num_tests, num_passed, num_failed, num_error  )