const form = document.getElementById("reservation-form");
const submitButton = document.getElementById("reserve");
const cancelButton = document.getElementById("cancel");
const roomSelect = document.getElementById("room");
const checkboxes = {
  period1: document.getElementById("period1"),
  period2: document.getElementById("period2"),
  period3: document.getElementById("period3"),
};
const studentInputs = [
  document.getElementById("student1"),
  document.getElementsByName("student2")[0],
  document.getElementsByName("student3")[0],
  document.getElementsByName("student4")[0],
  document.getElementsByName("student5")[0],
  document.getElementsByName("student6")[0],
];

const apiURL = "https://csiatech.kr/seminar/";



const retrieveCurrentReservation = () => {
  fetch(apiURL, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      type: "retrieve",
    },
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Failed to fetch current reservation");
      }
      return response.json();
    })
    .then((data) => {
      console.log(data);

      if (data.status === "reserved") {
        // Populate form with reservation data
        roomSelect.value = data.room_number;
        studentInputs[0].value = data.student1;
        studentInputs[1].value = data.student2;
        studentInputs[2].value = data.student3;
        studentInputs[3].value = data.student4;
        studentInputs[4].value = data.student5;
        studentInputs[5].value = data.student6;
        checkboxes.period1.checked = data.period1;
        checkboxes.period2.checked = data.period2;
        checkboxes.period3.checked = data.period3;

        if (!checkboxes.period1.checked) checkboxes.period1.disabled = true;
        if (!checkboxes.period2.checked) checkboxes.period2.disabled = true;
        if (!checkboxes.period3.checked) checkboxes.period3.disabled = true;

        cancelButton.style.display = "block";
        submitButton.style.display = "none";

        studentInputs.forEach((input) => {
          input.readOnly = true;
        });

        const roomStatus = data.room_status;
        Object.keys(roomStatus).forEach((roomNumber) => {
          const roomPeriods = roomStatus[roomNumber];
          for (let period = 1; period <= 3; period++) {
            const periodElement = document.getElementById(
              `room-${roomNumber}-${period}`
            );
            periodElement.style.backgroundColor = roomPeriods[`period${period}`]
              ? "lightcoral"
              : "lightgreen";
          }
        });
        cancelButton.style.display = "block";
        submitButton.style.display = "none";
      } else {
        const roomStatus = data.room_status;
        Object.keys(roomStatus).forEach((roomNumber) => {
          const roomPeriods = roomStatus[roomNumber];
          for (let period = 1; period <= 3; period++) {
            const periodElement = document.getElementById(
              `room-${roomNumber}-${period}`
            );
            periodElement.style.backgroundColor = roomPeriods[`period${period}`]
              ? "lightcoral"
              : "lightgreen";
          }
        });
        cancelButton.style.display = "none";
        submitButton.style.display = "block";
      }
      updateCheckboxesForRoom(roomSelect.value, data.room_status);
    })
    .catch((error) => {
      console.error("Error in retrieveCurrentReservation:", error);
    });
};

roomSelect.addEventListener("change", (event) => {
  // Check if any of the period checkboxes have been modified
  if (checkboxes.period1.checked || checkboxes.period2.checked || checkboxes.period3.checked) {
    alert("You cannot change the room after selecting any period.");
    event.preventDefault(); // Prevents the change event
    roomSelect.value = roomSelect.dataset.previousValue; // Restore the previous value
  } else {
    roomSelect.dataset.previousValue = roomSelect.value; // Store the new value
  }
});

document.addEventListener("DOMContentLoaded", () => {
  retrieveCurrentReservation();
  roomSelect.dataset.previousValue = roomSelect.value; // Store initial room value
});


function updateCheckboxesForRoom(roomNumber, roomStatus) {
  const roomPeriods = roomStatus[roomNumber];
  console.log(roomPeriods);

  // Update checkboxes for room periods
  checkboxes.period1.disabled = roomPeriods.period1;
  checkboxes.period2.disabled = roomPeriods.period2;
  checkboxes.period3.disabled = roomPeriods.period3;

  // Apply styles based on availability
  checkboxes.period1.style.opacity = roomPeriods.period1 ? "1" : "0.4";
  checkboxes.period2.style.opacity = roomPeriods.period2 ? "1" : "0.4";
  checkboxes.period3.style.opacity = roomPeriods.period3 ? "1" : "0.4";
}

function gatherFormData() {
  const formData = {
    room_number: parseInt(roomSelect.value),
    student1: studentInputs[0].value,
    student2: studentInputs[1].value,
    student3: studentInputs[2].value,
    student4: studentInputs[3].value,
    student5: studentInputs[4].value,
    student6: studentInputs[5].value,
    period1: checkboxes.period1.checked,
    period2: checkboxes.period2.checked,
    period3: checkboxes.period3.checked,
  };
  console.log("Form Data:", formData);
  return formData;
}

const makeReservation = async () => {
  const reservationData = gatherFormData();
  fetch(apiURL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(reservationData),
  })
    .then((response) => {
      if (!response.ok) {
        // JSON으로 파싱 전에 에러 응답 메시지를 확인하고, 적절히 처리합니다.
        throw new Error(
          `Server error: ${response.status} ${response.statusText}`
        );
      }
      return response.json();
    })
    .then((data) => {
      console.log(data);
      console.log("got response");
      if (data.status === "reserved") {
      } else {
        console.error("Error", data);
      }
    })
    .catch((error) => {
      console.error("Error", error);
    });
};

const deleteReservation = async () => {
  const reservationData = gatherFormData();
  fetch(apiURL, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(reservationData),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Failed to delete reservation");
      }
      return response.json();
    })
    .catch((error) => {
      console.error("Error deleting reservation:", error);
      throw error; // Re-throw the error if you want to handle it later
    });
};

submitButton.addEventListener("click", async () => {
  if (
    studentInputs[0].value &&
    Object.values(checkboxes).some((checkbox) => checkbox.checked)
  ) {
    // Check if the first student input is not empty
    await makeReservation(); // Ensure makeReservation is awaited
    alert("Successfully reserved");
    location.reload();
  } else {
    alert("Please fill in the form.");
  }
});
cancelButton.addEventListener("click", async () => {
  deleteReservation();
  alert("Successfully canceled");
  location.reload();
});

document.addEventListener("DOMContentLoaded", () => {
  retrieveCurrentReservation();

  roomSelect.addEventListener("change", async (event) => {
    retrieveCurrentReservation();
  });
});