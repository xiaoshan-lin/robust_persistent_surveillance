;; Auto-generated. Do not edit!


(when (boundp 'test_msgs::floatlist)
  (if (not (find-package "TEST_MSGS"))
    (make-package "TEST_MSGS"))
  (shadow 'floatlist (find-package "TEST_MSGS")))
(unless (find-package "TEST_MSGS::FLOATLIST")
  (make-package "TEST_MSGS::FLOATLIST"))

(in-package "ROS")
;;//! \htmlinclude floatlist.msg.html


(defclass test_msgs::floatlist
  :super ros::object
  :slots (_type _x _y _idx ))

(defmethod test_msgs::floatlist
  (:init
   (&key
    ((:type __type) 0)
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:idx __idx) 0)
    )
   (send-super :init)
   (setq _type (round __type))
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _idx (round __idx))
   self)
  (:type
   (&optional __type)
   (if __type (setq _type __type)) _type)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:idx
   (&optional __idx)
   (if __idx (setq _idx __idx)) _idx)
  (:serialization-length
   ()
   (+
    ;; int8 _type
    1
    ;; float64 _x
    8
    ;; float64 _y
    8
    ;; int8 _idx
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int8 _type
       (write-byte _type s)
     ;; float64 _x
       (sys::poke _x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y
       (sys::poke _y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; int8 _idx
       (write-byte _idx s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int8 _type
     (setq _type (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _type 127) (setq _type (- _type 256)))
   ;; float64 _x
     (setq _x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; int8 _idx
     (setq _idx (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _idx 127) (setq _idx (- _idx 256)))
   ;;
   self)
  )

(setf (get test_msgs::floatlist :md5sum-) "eb0aebf20b775fdee3c748e774f21882")
(setf (get test_msgs::floatlist :datatype-) "test_msgs/floatlist")
(setf (get test_msgs::floatlist :definition-)
      "int8 type
float64 x
float64 y
int8 idx

")



(provide :test_msgs/floatlist "eb0aebf20b775fdee3c748e774f21882")


