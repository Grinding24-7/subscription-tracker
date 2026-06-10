async function loadDashboard() {

    const recurringResponse =
        await fetch("http://127.0.0.1:8000/recurring");

    const recurring =
        await recurringResponse.json();

    const spendingResponse =
        await fetch("http://127.0.0.1:8000/spending");

    const spending =
        await spendingResponse.json();

    const servicesContainer =
        document.getElementById("services");

    const summaryContainer =
        document.getElementById("summary");

    summaryContainer.innerHTML = `
        <div class="bg-blue-500 text-white p-4 rounded shadow">
            <h2 class="text-lg font-bold">
                Recurring Services
            </h2>
            <p class="text-3xl">
                ${recurring.length}
            </p>
        </div>

        <div class="bg-green-500 text-white p-4 rounded shadow">
            <h2 class="text-lg font-bold">
                Estimated Spend
            </h2>
            <p class="text-3xl">
                Rs ${spending.total_spend}
            </p>
        </div>

        <div class="bg-purple-500 text-white p-4 rounded shadow">
            <h2 class="text-lg font-bold">
                Top Sender
            </h2>
            <p class="text-xl">
                ${recurring[0]?.sender || "N/A"}
            </p>
        </div>
    `;

    servicesContainer.innerHTML = "";

    recurring.forEach(service => {

        servicesContainer.innerHTML += `
            <div class="bg-white p-4 rounded shadow">

                <h2 class="font-bold text-lg">
                    ${service.sender}
                </h2>

                <p class="text-gray-600">
                    Emails: ${service.count}
                </p>

                <p class="text-green-600 font-bold mt-2">
                    Confidence: ${service.confidence || 0}%
                </p>

            </div>
        `;
    });
}

loadDashboard();