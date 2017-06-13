#include <iostream>
#include <unordered_map>
#define limit 1073741824

int main ()
{
  std::unordered_map<int,int> mymap;
  int pre = 0,index=1; 
  std::cout<<50000<<std::endl;
  for(int i = 0 ; i<40000;i++){
		mymap[i]  = 1;
		std::cout << i << std::endl;
		//std::cout << mymap.bucket_count()<<std::endl;
		//mymap[mymap.bucket_count()] = 1;
		//index = 2;
		//pre = mymap.bucket_count();
	}
  int success  = 0;
  for (int i = 1 ; i<=10000;i++){
	if (62233 * i < limit){
        	std::cout << 62233 * i<<std::endl;
 		success = 62233*i;
	}
	else
		std::cout << success << std::endl; 
 }
	//std::cout<<"num : "<<i<<std::endl; 


  return 0;
}
