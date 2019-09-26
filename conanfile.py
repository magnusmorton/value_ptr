from conans import ConanFile, CMake, tools


class ValueptrConan(ConanFile):
    name = "value-ptr"
    version = "0.4"
    
    export_sources = "include/*"
    no_copy_source = True

    def package(self):
        self.copy("*.h")
