
(cl:in-package :asdf)

(defsystem "test_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "floatlist" :depends-on ("_package_floatlist"))
    (:file "_package_floatlist" :depends-on ("_package"))
    (:file "floatlist_1" :depends-on ("_package_floatlist_1"))
    (:file "_package_floatlist_1" :depends-on ("_package"))
    (:file "timelist" :depends-on ("_package_timelist"))
    (:file "_package_timelist" :depends-on ("_package"))
  ))