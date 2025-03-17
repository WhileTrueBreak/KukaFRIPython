import time
from jadeController.utils.kukaiiwaIKSolver import FastInverseKinematics, ForwardKinematics, InverseKinematics
from jadeController.utils.optimiseIK import optimiseFromXYZ, optimiseFromABC

n = 10
start_time = time.perf_counter_ns()
for i in range(n):
    joints = optimiseFromABC(0.5,0.5,90)
end_time = time.perf_counter_ns()
print("Time taken for Optimisation:", (end_time - start_time)/n/1000000, "milliseconds")
print("Total Time taken for Optimisation:", (end_time - start_time)/1000000, "milliseconds")
