
(cl:in-package :asdf)

(defsystem "sbus_bridge-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "SbusRosMessage" :depends-on ("_package_SbusRosMessage"))
    (:file "_package_SbusRosMessage" :depends-on ("_package"))
  ))