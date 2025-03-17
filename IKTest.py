import time
from jadeController.utils.kukaiiwaIKSolver import FastInverseKinematics, ForwardKinematics, InverseKinematics

# Define some joint values (example values)
joint_values = [0.0, -0.5, 0.5, -1.0, 1.0, -0.5, 0.5]

# Get the pose using forward kinematics
pose, r, rconf, _ = ForwardKinematics(joint_values)

# Measure the time taken to run inverse kinematics
start_time = time.perf_counter_ns()
for i in range(1000):
    ik_joint_values, _, _ = InverseKinematics(pose, r, rconf)
end_time = time.perf_counter_ns()

print("Time taken for IK:", (end_time - start_time)/1000, "nanoseconds")
print(ik_joint_values)

start_time = time.perf_counter_ns()
for i in range(1000):
    ik_joint_values = FastInverseKinematics(pose, r, rconf)
end_time = time.perf_counter_ns()

print("Time taken for FIK:", (end_time - start_time)/1000, "nanoseconds")
print(ik_joint_values)
