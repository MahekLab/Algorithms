//function sendPackets(packet, callback) {
//  console.log("Sending packet : ", packet.id);
//
//  setTimeout(() => {
//    if (packet.status == "ACK") {
//      console.log(`Packet ${packet.id} recieved Successfully !`);
//      callback();
//    } else if (packet.status == "NACK") {
//      console.log(
//        `Packet ${packet.id} recieved with errors. Retransmitting...`,
//      );
//      setTimeout(() => {
//        console.log(`Retransmitted packet ${packet.id} Successfully !`);
//        callback();
//      }, 2000);
//    } else if (packet.status == "DELAY") {
//      console.log(`Packet ${packet.id} got delayed. Retransmitting...`);
//      setTimeout(() => {
//        console.log(`Packet ${packet.id} Retransmitted Successfully !`);
//        callback();
//      }, 2000);
//    }
//  }, 1000);
//}
//
//let packets = [
//  { id: 1, content: "Attack tonight", status: "ACK" },
//  { id: 2, content: "Attack cancled", status: "DELAY" },
//  { id: 3, content: "New plan", status: "NACK" },
//];
//
//function startTransmission(packets, index = 0) {
//  if (index < packets.length) {
//    sendPackets(packets[index], () => startTransmission(packets, index + 1));
//  } else {
//    console.log("All packets are sent.");
//  }
//}
//
//startTransmission(packets);

function reciever(packet, callback) {
  setTimeout(() => {
    if (Math.random() < 0.6) {
      packet.status = "ACK";
      console.log(`Packet ${packet.id} recieved Successfully !`);
    } else if (Math.random() < 0.8) {
      packet.status = "DELAY";
      console.log(`Packet ${packet.id} got delayed. Retransmit requested.`);
    } else {
      packet.status = "NACK";
      console.log(
        `Packet ${packet.id} found with errors. Retransmit requested.`,
      );
    }

    callback(packet.status);
  }, 1000);
}

function sendPackets(packet, callback) {
  console.log(`Sending packet ${packet.id}... `);
  reciever(packet, (status) => {
    if (status == "ACK") {
      console.log(`Packet ${packet.id} acknowledged !\n`);
      callback();
    } else if (status == "DELAY") {
      console.log(`Packet ${packet.id} delayed. Retransmitting...`);
      setTimeout(() => {
        console.log(`Retransmitted packet ${packet.id} Successfully !\n`);
        callback();
      }, 2000);
    } else if (status == "NACK") {
      console.log(
        `Packet ${packet.id} transmitted with errors. Retransmitting...`,
      );
      setTimeout(() => {
        console.log(`Packet ${packet.id} Retransmitted Successfully !\n`);
        callback();
      }, 2000);
    }
  });
}

function startTransmission(packets, index = 0) {
  if (index < packets.length) {
    sendPackets(packets[index], () => {
      startTransmission(packets, index + 1);
    });
  } else {
    console.log("All packets transmitted Successfully");
  }
}

let packets = [
  { id: 1, content: "Attack tonight", status: "DEFAULT" },
  { id: 2, content: "attack cancel", status: "DEFAULT" },
  { id: 3, content: "new plan", status: "DEFAULT" },
  { id: 4, content: "no attack", status: "DEFAULT" },
  { id: 5, content: "shanti jindabaad", status: "DEFAULT" },
];

startTransmission(packets);
