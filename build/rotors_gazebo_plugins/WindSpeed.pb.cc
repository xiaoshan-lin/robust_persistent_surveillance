// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: WindSpeed.proto

#define INTERNAL_SUPPRESS_PROTOBUF_FIELD_DEPRECATION
#include "WindSpeed.pb.h"

#include <algorithm>

#include <google/protobuf/stubs/common.h>
#include <google/protobuf/stubs/port.h>
#include <google/protobuf/stubs/once.h>
#include <google/protobuf/io/coded_stream.h>
#include <google/protobuf/wire_format_lite_inl.h>
#include <google/protobuf/descriptor.h>
#include <google/protobuf/generated_message_reflection.h>
#include <google/protobuf/reflection_ops.h>
#include <google/protobuf/wire_format.h>
// @@protoc_insertion_point(includes)

namespace gz_mav_msgs {

namespace {

const ::google::protobuf::Descriptor* WindSpeed_descriptor_ = NULL;
const ::google::protobuf::internal::GeneratedMessageReflection*
  WindSpeed_reflection_ = NULL;

}  // namespace


void protobuf_AssignDesc_WindSpeed_2eproto() GOOGLE_ATTRIBUTE_COLD;
void protobuf_AssignDesc_WindSpeed_2eproto() {
  protobuf_AddDesc_WindSpeed_2eproto();
  const ::google::protobuf::FileDescriptor* file =
    ::google::protobuf::DescriptorPool::generated_pool()->FindFileByName(
      "WindSpeed.proto");
  GOOGLE_CHECK(file != NULL);
  WindSpeed_descriptor_ = file->message_type(0);
  static const int WindSpeed_offsets_[2] = {
    GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(WindSpeed, header_),
    GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(WindSpeed, velocity_),
  };
  WindSpeed_reflection_ =
    ::google::protobuf::internal::GeneratedMessageReflection::NewGeneratedMessageReflection(
      WindSpeed_descriptor_,
      WindSpeed::default_instance_,
      WindSpeed_offsets_,
      GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(WindSpeed, _has_bits_[0]),
      -1,
      -1,
      sizeof(WindSpeed),
      GOOGLE_PROTOBUF_GENERATED_MESSAGE_FIELD_OFFSET(WindSpeed, _internal_metadata_),
      -1);
}

namespace {

GOOGLE_PROTOBUF_DECLARE_ONCE(protobuf_AssignDescriptors_once_);
inline void protobuf_AssignDescriptorsOnce() {
  ::google::protobuf::GoogleOnceInit(&protobuf_AssignDescriptors_once_,
                 &protobuf_AssignDesc_WindSpeed_2eproto);
}

void protobuf_RegisterTypes(const ::std::string&) GOOGLE_ATTRIBUTE_COLD;
void protobuf_RegisterTypes(const ::std::string&) {
  protobuf_AssignDescriptorsOnce();
  ::google::protobuf::MessageFactory::InternalRegisterGeneratedMessage(
      WindSpeed_descriptor_, &WindSpeed::default_instance());
}

}  // namespace

void protobuf_ShutdownFile_WindSpeed_2eproto() {
  delete WindSpeed::default_instance_;
  delete WindSpeed_reflection_;
}

void protobuf_AddDesc_WindSpeed_2eproto() GOOGLE_ATTRIBUTE_COLD;
void protobuf_AddDesc_WindSpeed_2eproto() {
  static bool already_here = false;
  if (already_here) return;
  already_here = true;
  GOOGLE_PROTOBUF_VERIFY_VERSION;

  ::gz_std_msgs::protobuf_AddDesc_Header_2eproto();
  ::gazebo::msgs::protobuf_AddDesc_vector3d_2eproto();
  ::google::protobuf::DescriptorPool::InternalAddGeneratedFile(
    "\n\017WindSpeed.proto\022\013gz_mav_msgs\032\014Header.p"
    "roto\032\016vector3d.proto\"Y\n\tWindSpeed\022#\n\006hea"
    "der\030\001 \002(\0132\023.gz_std_msgs.Header\022\'\n\010veloci"
    "ty\030\002 \002(\0132\025.gazebo.msgs.Vector3d", 151);
  ::google::protobuf::MessageFactory::InternalRegisterGeneratedFile(
    "WindSpeed.proto", &protobuf_RegisterTypes);
  WindSpeed::default_instance_ = new WindSpeed();
  WindSpeed::default_instance_->InitAsDefaultInstance();
  ::google::protobuf::internal::OnShutdown(&protobuf_ShutdownFile_WindSpeed_2eproto);
}

// Force AddDescriptors() to be called at static initialization time.
struct StaticDescriptorInitializer_WindSpeed_2eproto {
  StaticDescriptorInitializer_WindSpeed_2eproto() {
    protobuf_AddDesc_WindSpeed_2eproto();
  }
} static_descriptor_initializer_WindSpeed_2eproto_;

// ===================================================================

#if !defined(_MSC_VER) || _MSC_VER >= 1900
const int WindSpeed::kHeaderFieldNumber;
const int WindSpeed::kVelocityFieldNumber;
#endif  // !defined(_MSC_VER) || _MSC_VER >= 1900

WindSpeed::WindSpeed()
  : ::google::protobuf::Message(), _internal_metadata_(NULL) {
  SharedCtor();
  // @@protoc_insertion_point(constructor:gz_mav_msgs.WindSpeed)
}

void WindSpeed::InitAsDefaultInstance() {
  header_ = const_cast< ::gz_std_msgs::Header*>(&::gz_std_msgs::Header::default_instance());
  velocity_ = const_cast< ::gazebo::msgs::Vector3d*>(&::gazebo::msgs::Vector3d::default_instance());
}

WindSpeed::WindSpeed(const WindSpeed& from)
  : ::google::protobuf::Message(),
    _internal_metadata_(NULL) {
  SharedCtor();
  MergeFrom(from);
  // @@protoc_insertion_point(copy_constructor:gz_mav_msgs.WindSpeed)
}

void WindSpeed::SharedCtor() {
  _cached_size_ = 0;
  header_ = NULL;
  velocity_ = NULL;
  ::memset(_has_bits_, 0, sizeof(_has_bits_));
}

WindSpeed::~WindSpeed() {
  // @@protoc_insertion_point(destructor:gz_mav_msgs.WindSpeed)
  SharedDtor();
}

void WindSpeed::SharedDtor() {
  if (this != default_instance_) {
    delete header_;
    delete velocity_;
  }
}

void WindSpeed::SetCachedSize(int size) const {
  GOOGLE_SAFE_CONCURRENT_WRITES_BEGIN();
  _cached_size_ = size;
  GOOGLE_SAFE_CONCURRENT_WRITES_END();
}
const ::google::protobuf::Descriptor* WindSpeed::descriptor() {
  protobuf_AssignDescriptorsOnce();
  return WindSpeed_descriptor_;
}

const WindSpeed& WindSpeed::default_instance() {
  if (default_instance_ == NULL) protobuf_AddDesc_WindSpeed_2eproto();
  return *default_instance_;
}

WindSpeed* WindSpeed::default_instance_ = NULL;

WindSpeed* WindSpeed::New(::google::protobuf::Arena* arena) const {
  WindSpeed* n = new WindSpeed;
  if (arena != NULL) {
    arena->Own(n);
  }
  return n;
}

void WindSpeed::Clear() {
// @@protoc_insertion_point(message_clear_start:gz_mav_msgs.WindSpeed)
  if (_has_bits_[0 / 32] & 3u) {
    if (has_header()) {
      if (header_ != NULL) header_->::gz_std_msgs::Header::Clear();
    }
    if (has_velocity()) {
      if (velocity_ != NULL) velocity_->::gazebo::msgs::Vector3d::Clear();
    }
  }
  ::memset(_has_bits_, 0, sizeof(_has_bits_));
  if (_internal_metadata_.have_unknown_fields()) {
    mutable_unknown_fields()->Clear();
  }
}

bool WindSpeed::MergePartialFromCodedStream(
    ::google::protobuf::io::CodedInputStream* input) {
#define DO_(EXPRESSION) if (!GOOGLE_PREDICT_TRUE(EXPRESSION)) goto failure
  ::google::protobuf::uint32 tag;
  // @@protoc_insertion_point(parse_start:gz_mav_msgs.WindSpeed)
  for (;;) {
    ::std::pair< ::google::protobuf::uint32, bool> p = input->ReadTagWithCutoff(127);
    tag = p.first;
    if (!p.second) goto handle_unusual;
    switch (::google::protobuf::internal::WireFormatLite::GetTagFieldNumber(tag)) {
      // required .gz_std_msgs.Header header = 1;
      case 1: {
        if (tag == 10) {
          DO_(::google::protobuf::internal::WireFormatLite::ReadMessageNoVirtual(
               input, mutable_header()));
        } else {
          goto handle_unusual;
        }
        if (input->ExpectTag(18)) goto parse_velocity;
        break;
      }

      // required .gazebo.msgs.Vector3d velocity = 2;
      case 2: {
        if (tag == 18) {
         parse_velocity:
          DO_(::google::protobuf::internal::WireFormatLite::ReadMessageNoVirtual(
               input, mutable_velocity()));
        } else {
          goto handle_unusual;
        }
        if (input->ExpectAtEnd()) goto success;
        break;
      }

      default: {
      handle_unusual:
        if (tag == 0 ||
            ::google::protobuf::internal::WireFormatLite::GetTagWireType(tag) ==
            ::google::protobuf::internal::WireFormatLite::WIRETYPE_END_GROUP) {
          goto success;
        }
        DO_(::google::protobuf::internal::WireFormat::SkipField(
              input, tag, mutable_unknown_fields()));
        break;
      }
    }
  }
success:
  // @@protoc_insertion_point(parse_success:gz_mav_msgs.WindSpeed)
  return true;
failure:
  // @@protoc_insertion_point(parse_failure:gz_mav_msgs.WindSpeed)
  return false;
#undef DO_
}

void WindSpeed::SerializeWithCachedSizes(
    ::google::protobuf::io::CodedOutputStream* output) const {
  // @@protoc_insertion_point(serialize_start:gz_mav_msgs.WindSpeed)
  // required .gz_std_msgs.Header header = 1;
  if (has_header()) {
    ::google::protobuf::internal::WireFormatLite::WriteMessageMaybeToArray(
      1, *this->header_, output);
  }

  // required .gazebo.msgs.Vector3d velocity = 2;
  if (has_velocity()) {
    ::google::protobuf::internal::WireFormatLite::WriteMessageMaybeToArray(
      2, *this->velocity_, output);
  }

  if (_internal_metadata_.have_unknown_fields()) {
    ::google::protobuf::internal::WireFormat::SerializeUnknownFields(
        unknown_fields(), output);
  }
  // @@protoc_insertion_point(serialize_end:gz_mav_msgs.WindSpeed)
}

::google::protobuf::uint8* WindSpeed::InternalSerializeWithCachedSizesToArray(
    bool deterministic, ::google::protobuf::uint8* target) const {
  // @@protoc_insertion_point(serialize_to_array_start:gz_mav_msgs.WindSpeed)
  // required .gz_std_msgs.Header header = 1;
  if (has_header()) {
    target = ::google::protobuf::internal::WireFormatLite::
      InternalWriteMessageNoVirtualToArray(
        1, *this->header_, false, target);
  }

  // required .gazebo.msgs.Vector3d velocity = 2;
  if (has_velocity()) {
    target = ::google::protobuf::internal::WireFormatLite::
      InternalWriteMessageNoVirtualToArray(
        2, *this->velocity_, false, target);
  }

  if (_internal_metadata_.have_unknown_fields()) {
    target = ::google::protobuf::internal::WireFormat::SerializeUnknownFieldsToArray(
        unknown_fields(), target);
  }
  // @@protoc_insertion_point(serialize_to_array_end:gz_mav_msgs.WindSpeed)
  return target;
}

int WindSpeed::RequiredFieldsByteSizeFallback() const {
// @@protoc_insertion_point(required_fields_byte_size_fallback_start:gz_mav_msgs.WindSpeed)
  int total_size = 0;

  if (has_header()) {
    // required .gz_std_msgs.Header header = 1;
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::MessageSizeNoVirtual(
        *this->header_);
  }

  if (has_velocity()) {
    // required .gazebo.msgs.Vector3d velocity = 2;
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::MessageSizeNoVirtual(
        *this->velocity_);
  }

  return total_size;
}
int WindSpeed::ByteSize() const {
// @@protoc_insertion_point(message_byte_size_start:gz_mav_msgs.WindSpeed)
  int total_size = 0;

  if (((_has_bits_[0] & 0x00000003) ^ 0x00000003) == 0) {  // All required fields are present.
    // required .gz_std_msgs.Header header = 1;
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::MessageSizeNoVirtual(
        *this->header_);

    // required .gazebo.msgs.Vector3d velocity = 2;
    total_size += 1 +
      ::google::protobuf::internal::WireFormatLite::MessageSizeNoVirtual(
        *this->velocity_);

  } else {
    total_size += RequiredFieldsByteSizeFallback();
  }
  if (_internal_metadata_.have_unknown_fields()) {
    total_size +=
      ::google::protobuf::internal::WireFormat::ComputeUnknownFieldsSize(
        unknown_fields());
  }
  GOOGLE_SAFE_CONCURRENT_WRITES_BEGIN();
  _cached_size_ = total_size;
  GOOGLE_SAFE_CONCURRENT_WRITES_END();
  return total_size;
}

void WindSpeed::MergeFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_merge_from_start:gz_mav_msgs.WindSpeed)
  if (GOOGLE_PREDICT_FALSE(&from == this)) {
    ::google::protobuf::internal::MergeFromFail(__FILE__, __LINE__);
  }
  const WindSpeed* source = 
      ::google::protobuf::internal::DynamicCastToGenerated<const WindSpeed>(
          &from);
  if (source == NULL) {
  // @@protoc_insertion_point(generalized_merge_from_cast_fail:gz_mav_msgs.WindSpeed)
    ::google::protobuf::internal::ReflectionOps::Merge(from, this);
  } else {
  // @@protoc_insertion_point(generalized_merge_from_cast_success:gz_mav_msgs.WindSpeed)
    MergeFrom(*source);
  }
}

void WindSpeed::MergeFrom(const WindSpeed& from) {
// @@protoc_insertion_point(class_specific_merge_from_start:gz_mav_msgs.WindSpeed)
  if (GOOGLE_PREDICT_FALSE(&from == this)) {
    ::google::protobuf::internal::MergeFromFail(__FILE__, __LINE__);
  }
  if (from._has_bits_[0 / 32] & (0xffu << (0 % 32))) {
    if (from.has_header()) {
      mutable_header()->::gz_std_msgs::Header::MergeFrom(from.header());
    }
    if (from.has_velocity()) {
      mutable_velocity()->::gazebo::msgs::Vector3d::MergeFrom(from.velocity());
    }
  }
  if (from._internal_metadata_.have_unknown_fields()) {
    mutable_unknown_fields()->MergeFrom(from.unknown_fields());
  }
}

void WindSpeed::CopyFrom(const ::google::protobuf::Message& from) {
// @@protoc_insertion_point(generalized_copy_from_start:gz_mav_msgs.WindSpeed)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

void WindSpeed::CopyFrom(const WindSpeed& from) {
// @@protoc_insertion_point(class_specific_copy_from_start:gz_mav_msgs.WindSpeed)
  if (&from == this) return;
  Clear();
  MergeFrom(from);
}

bool WindSpeed::IsInitialized() const {
  if ((_has_bits_[0] & 0x00000003) != 0x00000003) return false;

  if (has_header()) {
    if (!this->header_->IsInitialized()) return false;
  }
  if (has_velocity()) {
    if (!this->velocity_->IsInitialized()) return false;
  }
  return true;
}

void WindSpeed::Swap(WindSpeed* other) {
  if (other == this) return;
  InternalSwap(other);
}
void WindSpeed::InternalSwap(WindSpeed* other) {
  std::swap(header_, other->header_);
  std::swap(velocity_, other->velocity_);
  std::swap(_has_bits_[0], other->_has_bits_[0]);
  _internal_metadata_.Swap(&other->_internal_metadata_);
  std::swap(_cached_size_, other->_cached_size_);
}

::google::protobuf::Metadata WindSpeed::GetMetadata() const {
  protobuf_AssignDescriptorsOnce();
  ::google::protobuf::Metadata metadata;
  metadata.descriptor = WindSpeed_descriptor_;
  metadata.reflection = WindSpeed_reflection_;
  return metadata;
}

#if PROTOBUF_INLINE_NOT_IN_HEADERS
// WindSpeed

// required .gz_std_msgs.Header header = 1;
bool WindSpeed::has_header() const {
  return (_has_bits_[0] & 0x00000001u) != 0;
}
void WindSpeed::set_has_header() {
  _has_bits_[0] |= 0x00000001u;
}
void WindSpeed::clear_has_header() {
  _has_bits_[0] &= ~0x00000001u;
}
void WindSpeed::clear_header() {
  if (header_ != NULL) header_->::gz_std_msgs::Header::Clear();
  clear_has_header();
}
const ::gz_std_msgs::Header& WindSpeed::header() const {
  // @@protoc_insertion_point(field_get:gz_mav_msgs.WindSpeed.header)
  return header_ != NULL ? *header_ : *default_instance_->header_;
}
::gz_std_msgs::Header* WindSpeed::mutable_header() {
  set_has_header();
  if (header_ == NULL) {
    header_ = new ::gz_std_msgs::Header;
  }
  // @@protoc_insertion_point(field_mutable:gz_mav_msgs.WindSpeed.header)
  return header_;
}
::gz_std_msgs::Header* WindSpeed::release_header() {
  // @@protoc_insertion_point(field_release:gz_mav_msgs.WindSpeed.header)
  clear_has_header();
  ::gz_std_msgs::Header* temp = header_;
  header_ = NULL;
  return temp;
}
void WindSpeed::set_allocated_header(::gz_std_msgs::Header* header) {
  delete header_;
  header_ = header;
  if (header) {
    set_has_header();
  } else {
    clear_has_header();
  }
  // @@protoc_insertion_point(field_set_allocated:gz_mav_msgs.WindSpeed.header)
}

// required .gazebo.msgs.Vector3d velocity = 2;
bool WindSpeed::has_velocity() const {
  return (_has_bits_[0] & 0x00000002u) != 0;
}
void WindSpeed::set_has_velocity() {
  _has_bits_[0] |= 0x00000002u;
}
void WindSpeed::clear_has_velocity() {
  _has_bits_[0] &= ~0x00000002u;
}
void WindSpeed::clear_velocity() {
  if (velocity_ != NULL) velocity_->::gazebo::msgs::Vector3d::Clear();
  clear_has_velocity();
}
const ::gazebo::msgs::Vector3d& WindSpeed::velocity() const {
  // @@protoc_insertion_point(field_get:gz_mav_msgs.WindSpeed.velocity)
  return velocity_ != NULL ? *velocity_ : *default_instance_->velocity_;
}
::gazebo::msgs::Vector3d* WindSpeed::mutable_velocity() {
  set_has_velocity();
  if (velocity_ == NULL) {
    velocity_ = new ::gazebo::msgs::Vector3d;
  }
  // @@protoc_insertion_point(field_mutable:gz_mav_msgs.WindSpeed.velocity)
  return velocity_;
}
::gazebo::msgs::Vector3d* WindSpeed::release_velocity() {
  // @@protoc_insertion_point(field_release:gz_mav_msgs.WindSpeed.velocity)
  clear_has_velocity();
  ::gazebo::msgs::Vector3d* temp = velocity_;
  velocity_ = NULL;
  return temp;
}
void WindSpeed::set_allocated_velocity(::gazebo::msgs::Vector3d* velocity) {
  delete velocity_;
  velocity_ = velocity;
  if (velocity) {
    set_has_velocity();
  } else {
    clear_has_velocity();
  }
  // @@protoc_insertion_point(field_set_allocated:gz_mav_msgs.WindSpeed.velocity)
}

#endif  // PROTOBUF_INLINE_NOT_IN_HEADERS

// @@protoc_insertion_point(namespace_scope)

}  // namespace gz_mav_msgs

// @@protoc_insertion_point(global_scope)