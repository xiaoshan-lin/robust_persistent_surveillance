;; Auto-generated. Do not edit!


(when (boundp 'sbus_bridge::SbusRosMessage)
  (if (not (find-package "SBUS_BRIDGE"))
    (make-package "SBUS_BRIDGE"))
  (shadow 'SbusRosMessage (find-package "SBUS_BRIDGE")))
(unless (find-package "SBUS_BRIDGE::SBUSROSMESSAGE")
  (make-package "SBUS_BRIDGE::SBUSROSMESSAGE"))

(in-package "ROS")
;;//! \htmlinclude SbusRosMessage.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass sbus_bridge::SbusRosMessage
  :super ros::object
  :slots (_header _channels _digital_channel_1 _digital_channel_2 _frame_lost _failsafe ))

(defmethod sbus_bridge::SbusRosMessage
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:channels __channels) (make-array 16 :initial-element 0 :element-type :integer))
    ((:digital_channel_1 __digital_channel_1) nil)
    ((:digital_channel_2 __digital_channel_2) nil)
    ((:frame_lost __frame_lost) nil)
    ((:failsafe __failsafe) nil)
    )
   (send-super :init)
   (setq _header __header)
   (setq _channels __channels)
   (setq _digital_channel_1 __digital_channel_1)
   (setq _digital_channel_2 __digital_channel_2)
   (setq _frame_lost __frame_lost)
   (setq _failsafe __failsafe)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:channels
   (&optional __channels)
   (if __channels (setq _channels __channels)) _channels)
  (:digital_channel_1
   (&optional __digital_channel_1)
   (if __digital_channel_1 (setq _digital_channel_1 __digital_channel_1)) _digital_channel_1)
  (:digital_channel_2
   (&optional __digital_channel_2)
   (if __digital_channel_2 (setq _digital_channel_2 __digital_channel_2)) _digital_channel_2)
  (:frame_lost
   (&optional __frame_lost)
   (if __frame_lost (setq _frame_lost __frame_lost)) _frame_lost)
  (:failsafe
   (&optional __failsafe)
   (if __failsafe (setq _failsafe __failsafe)) _failsafe)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; uint16[16] _channels
    (* 2    16)
    ;; bool _digital_channel_1
    1
    ;; bool _digital_channel_2
    1
    ;; bool _frame_lost
    1
    ;; bool _failsafe
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; uint16[16] _channels
     (dotimes (i 16)
       (write-word (elt _channels i) s)
       )
     ;; bool _digital_channel_1
       (if _digital_channel_1 (write-byte -1 s) (write-byte 0 s))
     ;; bool _digital_channel_2
       (if _digital_channel_2 (write-byte -1 s) (write-byte 0 s))
     ;; bool _frame_lost
       (if _frame_lost (write-byte -1 s) (write-byte 0 s))
     ;; bool _failsafe
       (if _failsafe (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; uint16[16] _channels
   (dotimes (i (length _channels))
     (setf (elt _channels i) (sys::peek buf ptr- :short)) (incf ptr- 2)
     )
   ;; bool _digital_channel_1
     (setq _digital_channel_1 (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _digital_channel_2
     (setq _digital_channel_2 (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _frame_lost
     (setq _frame_lost (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;; bool _failsafe
     (setq _failsafe (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(setf (get sbus_bridge::SbusRosMessage :md5sum-) "89ed6f5b79cb6f2d42c97b061bec3101")
(setf (get sbus_bridge::SbusRosMessage :datatype-) "sbus_bridge/SbusRosMessage")
(setf (get sbus_bridge::SbusRosMessage :definition-)
      "Header header

# Regular 16 sbus channels with 11 bit value range each
uint16[16] channels

# Digital channels
bool digital_channel_1
bool digital_channel_2

# Frame lost flag
bool frame_lost

# Failsafe flag
bool failsafe

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

")



(provide :sbus_bridge/SbusRosMessage "89ed6f5b79cb6f2d42c97b061bec3101")


