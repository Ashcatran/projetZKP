pragma solidity >=0.4.22 <0.6.0;

contract doctorList {
    
    //mapping (string => bool) public doctors;
    string[] doctors;
    
    function add(string memory _doc) public {
        doctors.push(_doc);
    }
    
    //function show() public view returns (string[] memory){
    //    return doctors;
    //}
    
    //from https://ethereum.stackexchange.com/questions/30912/how-to-compare-strings-in-solidity
    function compareStrings (string memory a, string memory  b) private pure returns (bool){
        return keccak256(abi.encode(a)) == keccak256(abi.encode(b));
    }
    
    function hasAccess(string memory _doc) public view returns (bool){
        bool access = false;
        for (uint i = 0; i < doctors.length; i++){
            if(compareStrings(doctors[i], _doc)){
                access = true;
            }
        }
        return access;
    }
    
}
