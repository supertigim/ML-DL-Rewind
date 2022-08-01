# for scipy installation
 export LDFLAGS="-L/opt/homebrew/opt/lapack/lib"
 export LDFLAGS="-L/opt/homebrew/opt/lapack/include"
 export LDFLAGS="-L/opt/homebrew/opt/lapack/lib"
 export CPPFLAGS="-L/opt/homebrew/opt/lapack/include"
 export PKG_CONFIG_PATH="-L/opt/homebrew/opt/lapack/pkgconfig"
 export CFLAGS=-Wno-error=implicit-function-declaration
 export LAPACK=/opt/homebrew/opt/lapack/lib/liblapack.dylib
 export BLAS=/opt/homebrew/opt/openblas/lib/libopenblasp-r0.3.20.dylib