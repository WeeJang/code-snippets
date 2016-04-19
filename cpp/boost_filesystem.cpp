// compile with -lboost_filesystem -lboost_system
#include <boost/filesystem.hpp>

int main(int argc, char *argv[])
{
    // check if a file exists
    if (!boost::filesystem::exists("boost_filesystem.cpp")) {
        std::cout << "file not exists" << std::endl;
    } else {
        std::cout << "file exists" << std::endl;
    }

    // remove a file
    boost::filesystem::remove("xx");
    
    return 0;
}

