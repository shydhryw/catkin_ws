execute_process(COMMAND "/home/shydh/catkin_ws/src/rbx2/rbx2_tasks/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/shydh/catkin_ws/src/rbx2/rbx2_tasks/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
