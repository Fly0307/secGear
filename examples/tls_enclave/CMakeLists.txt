# Copyright (c) Huawei Technologies Co., Ltd. 2020. All rights reserved.
# secGear is licensed under the Mulan PSL v2.
# You can use this software according to the terms and conditions of the Mulan PSL v2.
# You may obtain a copy of Mulan PSL v2 at:
#     http://license.coscl.org.cn/MulanPSL2
# THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND, EITHER EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT, MERCHANTABILITY OR FIT FOR A PARTICULAR
# PURPOSE.
# See the Mulan PSL v2 for more details.

project(TlsEnclave  C)

set(CMAKE_C_STANDARD 99)

set(CURRENT_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

#set edl name
set(EDL_FILE tls_enclave.edl)
#set auto code prefix
set(PREFIX tls_enclave)
set(CODEGEN codegen)

if (NOT DEFINED SSL_PATH)
	if(CC_SGX)
		set(SSL_PATH "/opt/intel/sgxssl")
	elseif(CC_GP)
		set(SSL_PATH "/opt/itrustee_sdk/itrustee_sdk_ssl")
    elseif(CC_PL)
        set(SSL_PATH "/root/dev/sdk/penglai_sdk_ssl")
        set(PL_SSLLIB_PATH "/opt/penglai/openssl")
	endif()
endif()

if(CC_SGX)
    set(CODETYPE sgx)
    add_definitions(-DPATH="${CMAKE_CURRENT_BINARY_DIR}/enclave/enclave.signed.so")
endif()

if(CC_PL)
    set(CODETYPE penglai)
    set(PL_SSLLIB_PATH "/opt/penglai/openssl")
    add_definitions(-DPATH="${CMAKE_CURRENT_SOURCE_DIR}/enclave/tls_penglai-ELF")
endif()

add_subdirectory(${CURRENT_ROOT_PATH}/enclave)
add_subdirectory(${CURRENT_ROOT_PATH}/host)
add_subdirectory(${CURRENT_ROOT_PATH}/client)
