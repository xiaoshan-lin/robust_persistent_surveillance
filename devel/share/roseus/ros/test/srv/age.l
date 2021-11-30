;; Auto-generated. Do not edit!


(when (boundp 'test::age)
  (if (not (find-package "TEST"))
    (make-package "TEST"))
  (shadow 'age (find-package "TEST")))
(unless (find-package "TEST::AGE")
  (make-package "TEST::AGE"))
(unless (find-package "TEST::AGEREQUEST")
  (make-package "TEST::AGEREQUEST"))
(unless (find-package "TEST::AGERESPONSE")
  (make-package "TEST::AGERESPONSE"))

(in-package "ROS")





(defclass test::ageRequest
  :super ros::object
  :slots (_data ))

(defmethod test::ageRequest
  (:init
   (&key
    ((:data __data) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _data __data)
   self)
  (:data
   (&optional __data)
   (if __data (setq _data __data)) _data)
  (:serialization-length
   ()
   (+
    ;; float32[] _data
    (* 4    (length _data)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32[] _data
     (write-long (length _data) s)
     (dotimes (i (length _data))
       (sys::poke (elt _data i) (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32[] _data
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _data (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _data i) (sys::peek buf ptr- :float)) (incf ptr- 4)
     ))
   ;;
   self)
  )

(defclass test::ageResponse
  :super ros::object
  :slots (_flag ))

(defmethod test::ageResponse
  (:init
   (&key
    ((:flag __flag) nil)
    )
   (send-super :init)
   (setq _flag __flag)
   self)
  (:flag
   (&optional __flag)
   (if __flag (setq _flag __flag)) _flag)
  (:serialization-length
   ()
   (+
    ;; bool _flag
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _flag
       (if _flag (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _flag
     (setq _flag (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass test::age
  :super ros::object
  :slots ())

(setf (get test::age :md5sum-) "f7eb1611265559a9d645d68293c29871")
(setf (get test::age :datatype-) "test/age")
(setf (get test::age :request) test::ageRequest)
(setf (get test::age :response) test::ageResponse)

(defmethod test::ageRequest
  (:response () (instance test::ageResponse :init)))

(setf (get test::ageRequest :md5sum-) "f7eb1611265559a9d645d68293c29871")
(setf (get test::ageRequest :datatype-) "test/ageRequest")
(setf (get test::ageRequest :definition-)
      "#request
float32[] data
---
#response
bool flag

")

(setf (get test::ageResponse :md5sum-) "f7eb1611265559a9d645d68293c29871")
(setf (get test::ageResponse :datatype-) "test/ageResponse")
(setf (get test::ageResponse :definition-)
      "#request
float32[] data
---
#response
bool flag

")



(provide :test/age "f7eb1611265559a9d645d68293c29871")


