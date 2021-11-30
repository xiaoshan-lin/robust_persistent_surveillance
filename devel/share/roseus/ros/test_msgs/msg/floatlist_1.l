;; Auto-generated. Do not edit!


(when (boundp 'test_msgs::floatlist_1)
  (if (not (find-package "TEST_MSGS"))
    (make-package "TEST_MSGS"))
  (shadow 'floatlist_1 (find-package "TEST_MSGS")))
(unless (find-package "TEST_MSGS::FLOATLIST_1")
  (make-package "TEST_MSGS::FLOATLIST_1"))

(in-package "ROS")
;;//! \htmlinclude floatlist_1.msg.html


(defclass test_msgs::floatlist_1
  :super ros::object
  :slots (_flag _x _y _idx ))

(defmethod test_msgs::floatlist_1
  (:init
   (&key
    ((:flag __flag) nil)
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:idx __idx) 0)
    )
   (send-super :init)
   (setq _flag __flag)
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _idx (round __idx))
   self)
  (:flag
   (&optional __flag)
   (if __flag (setq _flag __flag)) _flag)
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
    ;; bool _flag
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
     ;; bool _flag
       (if _flag (write-byte -1 s) (write-byte 0 s))
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
   ;; bool _flag
     (setq _flag (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
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

(setf (get test_msgs::floatlist_1 :md5sum-) "b14086f7038ce2afa371784cb7fd9953")
(setf (get test_msgs::floatlist_1 :datatype-) "test_msgs/floatlist_1")
(setf (get test_msgs::floatlist_1 :definition-)
      "bool flag
float64 x
float64 y
int8 idx

")



(provide :test_msgs/floatlist_1 "b14086f7038ce2afa371784cb7fd9953")


