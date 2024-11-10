from ai_engine.dialogue import Dialogue
from ai_engine.types import UAgentResponse, UAgentResponseType, KeyValue

class ChitChatDialogue(Dialogue):
    def __init__(self, version, storage=None):
        super().__init__(version=version, storage=storage)
        self.booking_type = None  # Track whether it's a hotel or flight booking
        self.booking_details = {}  # Store booking details
        print("ChitChatDialogue initialized")

    def on_initiate_session(self, model):
        print("Session initiated")
        return UAgentResponse(
            type=UAgentResponseType.FINAL,
            message="Hello! How can I assist you today?",
            request_id="initiate_001",
            agent_address="agent_001",
            options=[],
            verbose_message="Session initiation",
            verbose_options=[]
        )

    def on_continue_dialogue(self, user_message: str):
        print(f"Received user message: {user_message}")

        # Check if user is in the process of booking
        if self.booking_type:
            return self.collect_booking_details(user_message)

        # Check for booking request
        if "book" in user_message.lower():
            return UAgentResponse(
                type=UAgentResponseType.SELECT_FROM_OPTIONS,
                message="I can help you with bookings. What would you like to book?",
                request_id="booking_001",
                agent_address="agent_001",
                options=[
                    KeyValue(key="hotel", value="Hotel Booking"),
                    KeyValue(key="flight", value="Flight Booking")
                ],
                verbose_message="Offering booking options",
                verbose_options=[
                    KeyValue(key="hotel", value="Hotel Booking"),
                    KeyValue(key="flight", value="Flight Booking")
                ]
            )

        elif user_message.lower() == "hotel":
            self.booking_type = "hotel"
            self.booking_details = {}  # Reset booking details
            return UAgentResponse(
                type=UAgentResponseType.FINAL,
                message="Please provide the city for the hotel booking.",
                request_id="hotel_city_001",
                agent_address="agent_001",
                options=[],
                verbose_message="Collecting city for hotel booking",
                verbose_options=[]
            )

        elif user_message.lower() == "flight":
            self.booking_type = "flight"
            self.booking_details = {}  # Reset booking details
            return UAgentResponse(
                type=UAgentResponseType.FINAL,
                message="Please provide the departure city for the flight booking.",
                request_id="flight_departure_001",
                agent_address="agent_001",
                options=[],
                verbose_message="Collecting departure city for flight booking",
                verbose_options=[]
            )

        # Greeting response
        elif "hello" in user_message.lower() or "hi" in user_message.lower():
            return UAgentResponse(
                type=UAgentResponseType.FINAL,
                message="Hello! How are you today?",
                request_id="greeting_001",
                agent_address="agent_001",
                options=[],
                verbose_message="Greeting response",
                verbose_options=[]
            )

        # Fallback response if no match is found
        return UAgentResponse(
            type=UAgentResponseType.FINAL,
            message="I'm not sure how to respond to that. Can you clarify?",
            request_id="fallback_001",
            agent_address="agent_001",
            options=[],
            verbose_message="Fallback response",
            verbose_options=[]
        )

    def collect_booking_details(self, user_message: str):
        """Collect specific details for bookings based on the booking type."""
        if self.booking_type == "hotel":
            if not self.booking_details.get("city"):
                self.booking_details["city"] = user_message
                return UAgentResponse(
                    type=UAgentResponseType.FINAL,
                    message="Please provide the check-in date (e.g., 2024-12-01).",
                    request_id="hotel_checkin_001",
                    agent_address="agent_001",
                    options=[],
                    verbose_message="Collecting check-in date",
                    verbose_options=[]
                )
            elif not self.booking_details.get("check_in"):
                self.booking_details["check_in"] = user_message
                return UAgentResponse(
                    type=UAgentResponseType.FINAL,
                    message="Please provide the check-out date (e.g., 2024-12-05).",
                    request_id="hotel_checkout_001",
                    agent_address="agent_001",
                    options=[],
                    verbose_message="Collecting check-out date",
                    verbose_options=[]
                )
            elif not self.booking_details.get("check_out"):
                self.booking_details["check_out"] = user_message
                self.booking_type = None  # Reset booking type after completion
                return UAgentResponse(
                    type=UAgentResponseType.FINAL,
                    message=f"Hotel booked in {self.booking_details['city']} from {self.booking_details['check_in']} to {self.booking_details['check_out']}.",
                    request_id="hotel_confirm_001",
                    agent_address="agent_001",
                    options=[],
                    verbose_message="Hotel booking confirmed",
                    verbose_options=[]
                )

        return UAgentResponse(
            type=UAgentResponseType.FINAL,
            message="I'm having trouble understanding. Please try again.",
            request_id="error_001",
            agent_address="agent_001",
            options=[],
            verbose_message="Error in collecting details",
            verbose_options=[]
        )

    def on_end_session(self):
        print("Session ended")
        return UAgentResponse(
            type=UAgentResponseType.FINAL,
            message="Thank you for using our service! Goodbye.",
            request_id="end_001",
            agent_address="agent_001",
            options=[],
            verbose_message="Session ended",
            verbose_options=[]
        )
