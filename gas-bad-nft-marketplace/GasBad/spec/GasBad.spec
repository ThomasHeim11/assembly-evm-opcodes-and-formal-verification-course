/*
* Verification of GasBad
*/

persistent ghost mathint listingUpdateCount{
    init_state axiom listingUpdateCount == 0;
}
persistent ghost mathint log4Count{
    init_state axiom log4Count == 0;
}

hook Sstore s_listings[KEY address nftAddress][KEY uint256 tokenId].price uint256 price STORAGE {
    listingUpdatesCount = listingUpdatesCount + 1;
}

hook LOG4 (uint offset, uint length, bytes32 t1, bytes32 t2,bytes32 t3, bytes32 t4){
    log4Count = log4Count + 1;
}

/////////////////////////////////////////////////////////////////////
//                      Rules                                 //   //
/////////////////////////////////////////////////////////////////////
invariant anytime_mapping_update_event(){
    listingsUpdateCount <= log4Count;
}